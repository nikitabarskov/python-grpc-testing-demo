# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nikitabarskov/helloworld/v1beta1/hello_world.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n2nikitabarskov/helloworld/v1beta1/hello_world.proto\x12 nikitabarskov.helloworld.v1beta1"%\n\x0fSayHelloRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name",\n\x10SayHelloResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message2\x89\x01\n\x0eGreeterService\x12w\n\x08SayHello\x12\x31.nikitabarskov.helloworld.v1beta1.SayHelloRequest\x1a\x32.nikitabarskov.helloworld.v1beta1.SayHelloResponse"\x00(\x01\x30\x01\x42\xd9\x01\n$com.nikitabarskov.helloworld.v1beta1B\x0fHelloWorldProtoP\x01\xa2\x02\x03NHX\xaa\x02 Nikitabarskov.Helloworld.V1beta1\xca\x02 Nikitabarskov\\Helloworld\\V1beta1\xe2\x02,Nikitabarskov\\Helloworld\\V1beta1\\GPBMetadata\xea\x02"Nikitabarskov::Helloworld::V1beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "nikitabarskov.helloworld.v1beta1.hello_world_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b'\n$com.nikitabarskov.helloworld.v1beta1B\017HelloWorldProtoP\001\242\002\003NHX\252\002 Nikitabarskov.Helloworld.V1beta1\312\002 Nikitabarskov\\Helloworld\\V1beta1\342\002,Nikitabarskov\\Helloworld\\V1beta1\\GPBMetadata\352\002"Nikitabarskov::Helloworld::V1beta1'
    _globals["_SAYHELLOREQUEST"]._serialized_start = 88
    _globals["_SAYHELLOREQUEST"]._serialized_end = 125
    _globals["_SAYHELLORESPONSE"]._serialized_start = 127
    _globals["_SAYHELLORESPONSE"]._serialized_end = 171
    _globals["_GREETERSERVICE"]._serialized_start = 174
    _globals["_GREETERSERVICE"]._serialized_end = 311
# @@protoc_insertion_point(module_scope)
