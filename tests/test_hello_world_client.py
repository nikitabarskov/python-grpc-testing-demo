import threading

import grpc
import grpc_testing
from grpc.framework.foundation import logging_pool

from nikitabarskov.sdk.client import HelloWorldClient
from nikitabarskov.helloworld.v1beta1 import hello_world_pb2, hello_world_pb2_grpc

class Pipe:
    def __init__(self):
        self._condition = threading.Condition()
        self._values = []
        self._open = True

    def __iter__(self):
        return self

    def _next(self):
        with self._condition:
            while True:
                if self._values:
                    return self._values.pop(0)
                elif not self._open:
                    raise StopIteration()
                else:
                    self._condition.wait()

    def __next__(self):  # (Python 3 Iterator Protocol)
        return self._next()

    def next(self):  # (Python 2 Iterator Protocol)
        return self._next()

    def add(self, value):
        with self._condition:
            self._values.append(value)
            self._condition.notify_all()

    def close(self):
        with self._condition:
            self._open = False
            self._condition.notify_all()


def stream_stream(stub: hello_world_pb2_grpc.GreeterServiceStub):
    request_pipe = Pipe()
    responses = stub.SayHello(iter(request_pipe))
    request_pipe.add(hello_world_pb2.SayHelloRequest(name="Nikita"))
    first_responses = next(responses)
    request_pipe.add(hello_world_pb2.SayHelloRequest(name="Michael"))
    second_responses = next(responses)
    request_pipe.close()
    try:
        next(responses)
    except StopIteration:
        unexpected_extra_response = False
    return "data"

def test_hello_world_client_say_hello() -> None:
    channel = grpc_testing.channel(
        [hello_world_pb2.DESCRIPTOR.services_by_name["GreeterService"]],
        grpc_testing.strict_real_time(),
    )

    stub = hello_world_pb2_grpc.GreeterServiceStub(channel)

    client_execution_thread_pool = logging_pool.pool(1)

    client_responses = client_execution_thread_pool.submit(
        stream_stream, stub
    )

    invocation_metadata, rpc = channel.take_stream_stream(
        hello_world_pb2.DESCRIPTOR.services_by_name["GreeterService"].methods_by_name[
            "SayHello"
        ],
    )

    first_request = rpc.take_request()
    print(first_request)
    rpc.send_response(hello_world_pb2.SayHelloResponse(message=f"Hello, Nikita!"))
    second_request = rpc.take_request()
    print(second_request)
    rpc.send_response(hello_world_pb2.SayHelloResponse(message=f"Hello, Nikita!"))
    rpc.requests_closed()
    rpc.terminate((), grpc.StatusCode.OK, "")
    application_return_value = client_responses.result()
    print(application_return_value)
