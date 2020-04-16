# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: runtime/runtime.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='runtime/runtime.proto',
  package='go.micro.runtime',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15runtime/runtime.proto\x12\x10go.micro.runtime\"\xa4\x01\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x39\n\x08metadata\x18\x04 \x03(\x0b\x32\'.go.micro.runtime.Service.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"J\n\x05\x45vent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"h\n\rCreateOptions\x12\x0f\n\x07\x63ommand\x18\x01 \x03(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\x12\x0b\n\x03\x65nv\x18\x03 \x03(\t\x12\x0e\n\x06output\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\r\n\x05image\x18\x06 \x01(\t\"m\n\rCreateRequest\x12*\n\x07service\x18\x01 \x01(\x0b\x32\x19.go.micro.runtime.Service\x12\x30\n\x07options\x18\x02 \x01(\x0b\x32\x1f.go.micro.runtime.CreateOptions\"\x10\n\x0e\x43reateResponse\"=\n\x0bReadOptions\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"=\n\x0bReadRequest\x12.\n\x07options\x18\x01 \x01(\x0b\x32\x1d.go.micro.runtime.ReadOptions\";\n\x0cReadResponse\x12+\n\x08services\x18\x01 \x03(\x0b\x32\x19.go.micro.runtime.Service\";\n\rDeleteRequest\x12*\n\x07service\x18\x01 \x01(\x0b\x32\x19.go.micro.runtime.Service\"\x10\n\x0e\x44\x65leteResponse\";\n\rUpdateRequest\x12*\n\x07service\x18\x01 \x01(\x0b\x32\x19.go.micro.runtime.Service\"\x10\n\x0eUpdateResponse\"\r\n\x0bListRequest\";\n\x0cListResponse\x12+\n\x08services\x18\x01 \x03(\x0b\x32\x19.go.micro.runtime.Service\"L\n\x0bLogsRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\x08\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\x12\r\n\x05since\x18\x04 \x01(\x03\"\x9d\x01\n\tLogRecord\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12;\n\x08metadata\x18\x02 \x03(\x0b\x32).go.micro.runtime.LogRecord.MetadataEntry\x12\x0f\n\x07message\x18\x03 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x87\x03\n\x07Runtime\x12M\n\x06\x43reate\x12\x1f.go.micro.runtime.CreateRequest\x1a .go.micro.runtime.CreateResponse\"\x00\x12G\n\x04Read\x12\x1d.go.micro.runtime.ReadRequest\x1a\x1e.go.micro.runtime.ReadResponse\"\x00\x12M\n\x06\x44\x65lete\x12\x1f.go.micro.runtime.DeleteRequest\x1a .go.micro.runtime.DeleteResponse\"\x00\x12M\n\x06Update\x12\x1f.go.micro.runtime.UpdateRequest\x1a .go.micro.runtime.UpdateResponse\"\x00\x12\x46\n\x04Logs\x12\x1d.go.micro.runtime.LogsRequest\x1a\x1b.go.micro.runtime.LogRecord\"\x00\x30\x01\x62\x06proto3')
)




_SERVICE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='go.micro.runtime.Service.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.runtime.Service.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='go.micro.runtime.Service.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=208,
)

_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='go.micro.runtime.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='go.micro.runtime.Service.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='go.micro.runtime.Service.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='go.micro.runtime.Service.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='go.micro.runtime.Service.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SERVICE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=208,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='go.micro.runtime.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='go.micro.runtime.Event.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='go.micro.runtime.Event.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.runtime.Event.service', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='go.micro.runtime.Event.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=284,
)


_CREATEOPTIONS = _descriptor.Descriptor(
  name='CreateOptions',
  full_name='go.micro.runtime.CreateOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='go.micro.runtime.CreateOptions.command', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='go.micro.runtime.CreateOptions.args', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='go.micro.runtime.CreateOptions.env', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='go.micro.runtime.CreateOptions.output', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='go.micro.runtime.CreateOptions.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='go.micro.runtime.CreateOptions.image', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=390,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='go.micro.runtime.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.runtime.CreateRequest.service', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='go.micro.runtime.CreateRequest.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=501,
)


_CREATERESPONSE = _descriptor.Descriptor(
  name='CreateResponse',
  full_name='go.micro.runtime.CreateResponse',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=519,
)


_READOPTIONS = _descriptor.Descriptor(
  name='ReadOptions',
  full_name='go.micro.runtime.ReadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.runtime.ReadOptions.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='go.micro.runtime.ReadOptions.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='go.micro.runtime.ReadOptions.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=582,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='go.micro.runtime.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='go.micro.runtime.ReadRequest.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=584,
  serialized_end=645,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='go.micro.runtime.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='go.micro.runtime.ReadResponse.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=706,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='go.micro.runtime.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.runtime.DeleteRequest.service', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=708,
  serialized_end=767,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='go.micro.runtime.DeleteResponse',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=769,
  serialized_end=785,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='go.micro.runtime.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.runtime.UpdateRequest.service', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=846,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='go.micro.runtime.UpdateResponse',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=848,
  serialized_end=864,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='go.micro.runtime.ListRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=879,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='go.micro.runtime.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='go.micro.runtime.ListResponse.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=940,
)


_LOGSREQUEST = _descriptor.Descriptor(
  name='LogsRequest',
  full_name='go.micro.runtime.LogsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.runtime.LogsRequest.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='go.micro.runtime.LogsRequest.stream', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='go.micro.runtime.LogsRequest.count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since', full_name='go.micro.runtime.LogsRequest.since', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=942,
  serialized_end=1018,
)


_LOGRECORD_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='go.micro.runtime.LogRecord.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='go.micro.runtime.LogRecord.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='go.micro.runtime.LogRecord.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=208,
)

_LOGRECORD = _descriptor.Descriptor(
  name='LogRecord',
  full_name='go.micro.runtime.LogRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='go.micro.runtime.LogRecord.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='go.micro.runtime.LogRecord.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='go.micro.runtime.LogRecord.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOGRECORD_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1021,
  serialized_end=1178,
)

_SERVICE_METADATAENTRY.containing_type = _SERVICE
_SERVICE.fields_by_name['metadata'].message_type = _SERVICE_METADATAENTRY
_CREATEREQUEST.fields_by_name['service'].message_type = _SERVICE
_CREATEREQUEST.fields_by_name['options'].message_type = _CREATEOPTIONS
_READREQUEST.fields_by_name['options'].message_type = _READOPTIONS
_READRESPONSE.fields_by_name['services'].message_type = _SERVICE
_DELETEREQUEST.fields_by_name['service'].message_type = _SERVICE
_UPDATEREQUEST.fields_by_name['service'].message_type = _SERVICE
_LISTRESPONSE.fields_by_name['services'].message_type = _SERVICE
_LOGRECORD_METADATAENTRY.containing_type = _LOGRECORD
_LOGRECORD.fields_by_name['metadata'].message_type = _LOGRECORD_METADATAENTRY
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['CreateOptions'] = _CREATEOPTIONS
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['ReadOptions'] = _READOPTIONS
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['LogsRequest'] = _LOGSREQUEST
DESCRIPTOR.message_types_by_name['LogRecord'] = _LOGRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _SERVICE_METADATAENTRY,
    __module__ = 'runtime.runtime_pb2'
    # @@protoc_insertion_point(class_scope:go.micro.runtime.Service.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _SERVICE,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.Service)
  ))
_sym_db.RegisterMessage(Service)
_sym_db.RegisterMessage(Service.MetadataEntry)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.Event)
  ))
_sym_db.RegisterMessage(Event)

CreateOptions = _reflection.GeneratedProtocolMessageType('CreateOptions', (_message.Message,), dict(
  DESCRIPTOR = _CREATEOPTIONS,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.CreateOptions)
  ))
_sym_db.RegisterMessage(CreateOptions)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATERESPONSE,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.CreateResponse)
  ))
_sym_db.RegisterMessage(CreateResponse)

ReadOptions = _reflection.GeneratedProtocolMessageType('ReadOptions', (_message.Message,), dict(
  DESCRIPTOR = _READOPTIONS,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.ReadOptions)
  ))
_sym_db.RegisterMessage(ReadOptions)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _READREQUEST,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.ReadRequest)
  ))
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), dict(
  DESCRIPTOR = _READRESPONSE,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.ReadResponse)
  ))
_sym_db.RegisterMessage(ReadResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETERESPONSE,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.DeleteResponse)
  ))
_sym_db.RegisterMessage(DeleteResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQUEST,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.UpdateRequest)
  ))
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATERESPONSE,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.UpdateResponse)
  ))
_sym_db.RegisterMessage(UpdateResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTREQUEST,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.ListRequest)
  ))
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESPONSE,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.ListResponse)
  ))
_sym_db.RegisterMessage(ListResponse)

LogsRequest = _reflection.GeneratedProtocolMessageType('LogsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGSREQUEST,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.LogsRequest)
  ))
_sym_db.RegisterMessage(LogsRequest)

LogRecord = _reflection.GeneratedProtocolMessageType('LogRecord', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _LOGRECORD_METADATAENTRY,
    __module__ = 'runtime.runtime_pb2'
    # @@protoc_insertion_point(class_scope:go.micro.runtime.LogRecord.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _LOGRECORD,
  __module__ = 'runtime.runtime_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.runtime.LogRecord)
  ))
_sym_db.RegisterMessage(LogRecord)
_sym_db.RegisterMessage(LogRecord.MetadataEntry)


_SERVICE_METADATAENTRY._options = None
_LOGRECORD_METADATAENTRY._options = None

_RUNTIME = _descriptor.ServiceDescriptor(
  name='Runtime',
  full_name='go.micro.runtime.Runtime',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1181,
  serialized_end=1572,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='go.micro.runtime.Runtime.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='go.micro.runtime.Runtime.Read',
    index=1,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='go.micro.runtime.Runtime.Delete',
    index=2,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='go.micro.runtime.Runtime.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Logs',
    full_name='go.micro.runtime.Runtime.Logs',
    index=4,
    containing_service=None,
    input_type=_LOGSREQUEST,
    output_type=_LOGRECORD,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RUNTIME)

DESCRIPTOR.services_by_name['Runtime'] = _RUNTIME

# @@protoc_insertion_point(module_scope)
