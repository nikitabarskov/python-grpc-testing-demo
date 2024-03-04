from dataclasses import dataclass
from typing import Iterable

import grpc

from nikitabarskov.helloworld.v1beta1 import hello_world_pb2_grpc
from nikitabarskov.helloworld.v1beta1 import hello_world_pb2


@dataclass
class HelloWorldClient:
    channel: grpc.Channel

    def say_hello(self: "HelloWorldClient", messages: Iterable[str]) -> Iterable[str]:
        stub = hello_world_pb2_grpc.GreeterServiceStub(self.channel)
        for response in stub.SayHello(self._generate_requests(messages)):
            yield response.message

    @staticmethod
    def _generate_requests(
        messages: Iterable[str],
    ) -> Iterable[hello_world_pb2.SayHelloRequest]:
        for message in messages:
            yield hello_world_pb2.SayHelloRequest(name=message)
