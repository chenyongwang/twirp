# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: multiple2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='multiple2.proto',
  package='twirp.internal.twirptest.multiple',
  syntax='proto3',
  serialized_pb=_b('\n\x0fmultiple2.proto\x12!twirp.internal.twirptest.multiple\"\x06\n\x04Msg22`\n\x04Svc2\x12X\n\x04Send\x12\'.twirp.internal.twirptest.multiple.Msg2\x1a\'.twirp.internal.twirptest.multiple.Msg2B\nZ\x08multipleb\x06proto3')
)




_MSG2 = _descriptor.Descriptor(
  name='Msg2',
  full_name='twirp.internal.twirptest.multiple.Msg2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=60,
)

DESCRIPTOR.message_types_by_name['Msg2'] = _MSG2
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Msg2 = _reflection.GeneratedProtocolMessageType('Msg2', (_message.Message,), dict(
  DESCRIPTOR = _MSG2,
  __module__ = 'multiple2_pb2'
  # @@protoc_insertion_point(class_scope:twirp.internal.twirptest.multiple.Msg2)
  ))
_sym_db.RegisterMessage(Msg2)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\010multiple'))
# @@protoc_insertion_point(module_scope)
