# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: router/router.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='router/router.proto',
  package='go.micro.router',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13router/router.proto\x12\x0fgo.micro.router\"\t\n\x07Request\"\n\n\x08Response\"6\n\x0cListResponse\x12&\n\x06routes\x18\x01 \x03(\x0b\x32\x16.go.micro.router.Route\"6\n\rLookupRequest\x12%\n\x05query\x18\x01 \x01(\x0b\x32\x16.go.micro.router.Query\"8\n\x0eLookupResponse\x12&\n\x06routes\x18\x01 \x03(\x0b\x32\x16.go.micro.router.Route\"5\n\x0cQueryRequest\x12%\n\x05query\x18\x01 \x01(\x0b\x32\x16.go.micro.router.Query\"7\n\rQueryResponse\x12&\n\x06routes\x18\x01 \x03(\x0b\x32\x16.go.micro.router.Route\"\x0e\n\x0cWatchRequest\"\x87\x01\n\x06\x41\x64vert\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.go.micro.router.AdvertType\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x0b\n\x03ttl\x18\x04 \x01(\x03\x12&\n\x06\x65vents\x18\x05 \x03(\x0b\x32\x16.go.micro.router.Event\"\x11\n\x0fProcessResponse\"\x10\n\x0e\x43reateResponse\"\x10\n\x0e\x44\x65leteResponse\"\x10\n\x0eUpdateResponse\"w\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.go.micro.router.EventType\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12%\n\x05route\x18\x04 \x01(\x0b\x32\x16.go.micro.router.Route\":\n\x05Query\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07gateway\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\"y\n\x05Route\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0f\n\x07gateway\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0e\n\x06router\x18\x05 \x01(\t\x12\x0c\n\x04link\x18\x06 \x01(\t\x12\x0e\n\x06metric\x18\x07 \x01(\x03*2\n\nAdvertType\x12\x12\n\x0e\x41\x64vertAnnounce\x10\x00\x12\x10\n\x0c\x41\x64vertUpdate\x10\x01*/\n\tEventType\x12\n\n\x06\x43reate\x10\x00\x12\n\n\x06\x44\x65lete\x10\x01\x12\n\n\x06Update\x10\x02\x32\xa5\x02\n\x06Router\x12K\n\x06Lookup\x12\x1e.go.micro.router.LookupRequest\x1a\x1f.go.micro.router.LookupResponse\"\x00\x12\x42\n\x05Watch\x12\x1d.go.micro.router.WatchRequest\x1a\x16.go.micro.router.Event\"\x00\x30\x01\x12\x42\n\tAdvertise\x12\x18.go.micro.router.Request\x1a\x17.go.micro.router.Advert\"\x00\x30\x01\x12\x46\n\x07Process\x12\x17.go.micro.router.Advert\x1a .go.micro.router.ProcessResponse\"\x00\x32\xe3\x02\n\x05Table\x12\x43\n\x06\x43reate\x12\x16.go.micro.router.Route\x1a\x1f.go.micro.router.CreateResponse\"\x00\x12\x43\n\x06\x44\x65lete\x12\x16.go.micro.router.Route\x1a\x1f.go.micro.router.DeleteResponse\"\x00\x12\x43\n\x06Update\x12\x16.go.micro.router.Route\x1a\x1f.go.micro.router.UpdateResponse\"\x00\x12\x41\n\x04List\x12\x18.go.micro.router.Request\x1a\x1d.go.micro.router.ListResponse\"\x00\x12H\n\x05Query\x12\x1d.go.micro.router.QueryRequest\x1a\x1e.go.micro.router.QueryResponse\"\x00\x62\x06proto3'
)

_ADVERTTYPE = _descriptor.EnumDescriptor(
  name='AdvertType',
  full_name='go.micro.router.AdvertType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AdvertAnnounce', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AdvertUpdate', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=876,
  serialized_end=926,
)
_sym_db.RegisterEnumDescriptor(_ADVERTTYPE)

AdvertType = enum_type_wrapper.EnumTypeWrapper(_ADVERTTYPE)
_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='go.micro.router.EventType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Create', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Delete', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Update', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=928,
  serialized_end=975,
)
_sym_db.RegisterEnumDescriptor(_EVENTTYPE)

EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
AdvertAnnounce = 0
AdvertUpdate = 1
Create = 0
Delete = 1
Update = 2



_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='go.micro.router.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=40,
  serialized_end=49,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='go.micro.router.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=51,
  serialized_end=61,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='go.micro.router.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='routes', full_name='go.micro.router.ListResponse.routes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=63,
  serialized_end=117,
)


_LOOKUPREQUEST = _descriptor.Descriptor(
  name='LookupRequest',
  full_name='go.micro.router.LookupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='go.micro.router.LookupRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=119,
  serialized_end=173,
)


_LOOKUPRESPONSE = _descriptor.Descriptor(
  name='LookupResponse',
  full_name='go.micro.router.LookupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='routes', full_name='go.micro.router.LookupResponse.routes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=175,
  serialized_end=231,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='go.micro.router.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='go.micro.router.QueryRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=233,
  serialized_end=286,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='go.micro.router.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='routes', full_name='go.micro.router.QueryResponse.routes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=288,
  serialized_end=343,
)


_WATCHREQUEST = _descriptor.Descriptor(
  name='WatchRequest',
  full_name='go.micro.router.WatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=345,
  serialized_end=359,
)


_ADVERT = _descriptor.Descriptor(
  name='Advert',
  full_name='go.micro.router.Advert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='go.micro.router.Advert.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='go.micro.router.Advert.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='go.micro.router.Advert.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='go.micro.router.Advert.ttl', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='events', full_name='go.micro.router.Advert.events', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=362,
  serialized_end=497,
)


_PROCESSRESPONSE = _descriptor.Descriptor(
  name='ProcessResponse',
  full_name='go.micro.router.ProcessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=499,
  serialized_end=516,
)


_CREATERESPONSE = _descriptor.Descriptor(
  name='CreateResponse',
  full_name='go.micro.router.CreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=518,
  serialized_end=534,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='go.micro.router.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=536,
  serialized_end=552,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='go.micro.router.UpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=554,
  serialized_end=570,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='go.micro.router.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='go.micro.router.Event.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='go.micro.router.Event.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='go.micro.router.Event.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route', full_name='go.micro.router.Event.route', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=572,
  serialized_end=691,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='go.micro.router.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.router.Query.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='go.micro.router.Query.gateway', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='go.micro.router.Query.network', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=693,
  serialized_end=751,
)


_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='go.micro.router.Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='go.micro.router.Route.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='go.micro.router.Route.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='go.micro.router.Route.gateway', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='go.micro.router.Route.network', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='router', full_name='go.micro.router.Route.router', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='link', full_name='go.micro.router.Route.link', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric', full_name='go.micro.router.Route.metric', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=753,
  serialized_end=874,
)

_LISTRESPONSE.fields_by_name['routes'].message_type = _ROUTE
_LOOKUPREQUEST.fields_by_name['query'].message_type = _QUERY
_LOOKUPRESPONSE.fields_by_name['routes'].message_type = _ROUTE
_QUERYREQUEST.fields_by_name['query'].message_type = _QUERY
_QUERYRESPONSE.fields_by_name['routes'].message_type = _ROUTE
_ADVERT.fields_by_name['type'].enum_type = _ADVERTTYPE
_ADVERT.fields_by_name['events'].message_type = _EVENT
_EVENT.fields_by_name['type'].enum_type = _EVENTTYPE
_EVENT.fields_by_name['route'].message_type = _ROUTE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['LookupRequest'] = _LOOKUPREQUEST
DESCRIPTOR.message_types_by_name['LookupResponse'] = _LOOKUPRESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['WatchRequest'] = _WATCHREQUEST
DESCRIPTOR.message_types_by_name['Advert'] = _ADVERT
DESCRIPTOR.message_types_by_name['ProcessResponse'] = _PROCESSRESPONSE
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Route'] = _ROUTE
DESCRIPTOR.enum_types_by_name['AdvertType'] = _ADVERTTYPE
DESCRIPTOR.enum_types_by_name['EventType'] = _EVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.Response)
  })
_sym_db.RegisterMessage(Response)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

LookupRequest = _reflection.GeneratedProtocolMessageType('LookupRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPREQUEST,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.LookupRequest)
  })
_sym_db.RegisterMessage(LookupRequest)

LookupResponse = _reflection.GeneratedProtocolMessageType('LookupResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPRESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.LookupResponse)
  })
_sym_db.RegisterMessage(LookupResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

WatchRequest = _reflection.GeneratedProtocolMessageType('WatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHREQUEST,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.WatchRequest)
  })
_sym_db.RegisterMessage(WatchRequest)

Advert = _reflection.GeneratedProtocolMessageType('Advert', (_message.Message,), {
  'DESCRIPTOR' : _ADVERT,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.Advert)
  })
_sym_db.RegisterMessage(Advert)

ProcessResponse = _reflection.GeneratedProtocolMessageType('ProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSRESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.ProcessResponse)
  })
_sym_db.RegisterMessage(ProcessResponse)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.CreateResponse)
  })
_sym_db.RegisterMessage(CreateResponse)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.Event)
  })
_sym_db.RegisterMessage(Event)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.Query)
  })
_sym_db.RegisterMessage(Query)

Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
  'DESCRIPTOR' : _ROUTE,
  '__module__' : 'router.router_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.router.Route)
  })
_sym_db.RegisterMessage(Route)



_ROUTER = _descriptor.ServiceDescriptor(
  name='Router',
  full_name='go.micro.router.Router',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=978,
  serialized_end=1271,
  methods=[
  _descriptor.MethodDescriptor(
    name='Lookup',
    full_name='go.micro.router.Router.Lookup',
    index=0,
    containing_service=None,
    input_type=_LOOKUPREQUEST,
    output_type=_LOOKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Watch',
    full_name='go.micro.router.Router.Watch',
    index=1,
    containing_service=None,
    input_type=_WATCHREQUEST,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Advertise',
    full_name='go.micro.router.Router.Advertise',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_ADVERT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Process',
    full_name='go.micro.router.Router.Process',
    index=3,
    containing_service=None,
    input_type=_ADVERT,
    output_type=_PROCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTER)

DESCRIPTOR.services_by_name['Router'] = _ROUTER


_TABLE = _descriptor.ServiceDescriptor(
  name='Table',
  full_name='go.micro.router.Table',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1274,
  serialized_end=1629,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='go.micro.router.Table.Create',
    index=0,
    containing_service=None,
    input_type=_ROUTE,
    output_type=_CREATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='go.micro.router.Table.Delete',
    index=1,
    containing_service=None,
    input_type=_ROUTE,
    output_type=_DELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='go.micro.router.Table.Update',
    index=2,
    containing_service=None,
    input_type=_ROUTE,
    output_type=_UPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='go.micro.router.Table.List',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='go.micro.router.Table.Query',
    index=4,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TABLE)

DESCRIPTOR.services_by_name['Table'] = _TABLE

# @@protoc_insertion_point(module_scope)
