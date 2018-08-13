#!/usr/bin/env python
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ideacrawler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ideacrawler.proto',
  package='ideacrawler',
  syntax='proto3',
  serialized_pb=_b('\n\x11ideacrawler.proto\x12\x0bideacrawler\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"(\n\x06Status\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"!\n\x03KVP\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xbd\x07\n\tDomainOpt\x12\x0f\n\x07seedUrl\x18\x01 \x01(\t\x12\x10\n\x08minDelay\x18\x02 \x01(\x05\x12\x10\n\x08maxDelay\x18\x03 \x01(\x05\x12\x10\n\x08noFollow\x18\x04 \x01(\x08\x12\x19\n\x11\x63\x61llbackUrlRegexp\x18\x05 \x01(\t\x12\x17\n\x0f\x66ollowUrlRegexp\x18\x06 \x01(\t\x12\x1d\n\x15maxConcurrentRequests\x18\x07 \x01(\x05\x12\x11\n\tuseragent\x18\x08 \x01(\t\x12\x10\n\x08impolite\x18\t \x01(\x08\x12\r\n\x05\x64\x65pth\x18\n \x01(\x05\x12\x0e\n\x06repeat\x18\x0b \x01(\x08\x12,\n\tfrequency\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration\x12,\n\x08\x66irstrun\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x12\x63\x61llbackXpathMatch\x18\x0e \x03(\x0b\x32\x10.ideacrawler.KVP\x12-\n\x13\x63\x61llbackXpathRegexp\x18\x0f \x03(\x0b\x32\x10.ideacrawler.KVP\x12\x10\n\x08unused16\x18\x10 \x01(\x08\x12\x1a\n\x12\x66ollowOtherDomains\x18\x11 \x01(\x08\x12\x13\n\x0bkeepDomains\x18\x12 \x03(\t\x12\x13\n\x0b\x64ropDomains\x18\x13 \x03(\t\x12\x1a\n\x12\x64omainDropPriority\x18\x14 \x01(\x08\x12\x1a\n\x12unsafeNormalizeURL\x18\x15 \x01(\x08\x12\r\n\x05login\x18\x16 \x01(\x08\x12\x1a\n\x12loginUsingSelenium\x18\x17 \x01(\x08\x12\x10\n\x08loginUrl\x18\x18 \x01(\t\x12&\n\x0cloginPayload\x18\x19 \x03(\x0b\x32\x10.ideacrawler.KVP\x12\x18\n\x10loginParseFields\x18\x1a \x01(\x08\x12)\n\x0floginParseXpath\x18\x1b \x03(\x0b\x32\x10.ideacrawler.KVP\x12+\n\x11loginSuccessCheck\x18\x1c \x01(\x0b\x32\x10.ideacrawler.KVP\x12\x1f\n\x17\x63heckLoginAfterEachPage\x18\x1d \x01(\x08\x12\x0e\n\x06unused\x18\x1e \x01(\x08\x12\x0e\n\x06\x63hrome\x18\x1f \x01(\x08\x12\x14\n\x0c\x63hromeBinary\x18  \x01(\t\x12\x13\n\x0b\x64omLoadTime\x18! \x01(\x05\x12\x14\n\x0cnetworkIface\x18\" \x01(\t\x12\x1a\n\x12\x63\x61ncelOnDisconnect\x18# \x01(\x08\x12\x14\n\x0c\x63heckContent\x18$ \x01(\x08\"\x98\x01\n\x0cSubscription\x12\x0f\n\x07subcode\x18\x01 \x01(\t\x12\x12\n\ndomainname\x18\x02 \x01(\t\x12%\n\x07subtype\x18\x03 \x01(\x0e\x32\x14.ideacrawler.SubType\x12\x0e\n\x06seqnum\x18\x04 \x01(\x05\x12,\n\x08\x64\x61tetime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"~\n\x0bPageRequest\x12&\n\x03sub\x18\x01 \x01(\x0b\x32\x19.ideacrawler.Subscription\x12)\n\x07reqtype\x18\x02 \x01(\x0e\x32\x18.ideacrawler.PageReqType\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07metaStr\x18\x04 \x01(\t\"\x99\x01\n\x08PageHTML\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12&\n\x03sub\x18\x03 \x01(\x0b\x32\x19.ideacrawler.Subscription\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x16\n\x0ehttpstatuscode\x18\x05 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\x0c\x12\x0f\n\x07metaStr\x18\x07 \x01(\t*#\n\x07SubType\x12\n\n\x06SEQNUM\x10\x00\x12\x0c\n\x08\x44\x41TETIME\x10\x01* \n\x0bPageReqType\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04HEAD\x10\x01\x32\xd4\x01\n\x0bIdeaCrawler\x12G\n\x12\x41\x64\x64\x44omainAndListen\x12\x16.ideacrawler.DomainOpt\x1a\x15.ideacrawler.PageHTML\"\x00\x30\x01\x12=\n\x08\x41\x64\x64Pages\x12\x18.ideacrawler.PageRequest\x1a\x13.ideacrawler.Status\"\x00(\x01\x12=\n\tCancelJob\x12\x19.ideacrawler.Subscription\x1a\x13.ideacrawler.Status\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])

_SUBTYPE = _descriptor.EnumDescriptor(
  name='SubType',
  full_name='ideacrawler.SubType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEQNUM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1575,
  serialized_end=1610,
)
_sym_db.RegisterEnumDescriptor(_SUBTYPE)

SubType = enum_type_wrapper.EnumTypeWrapper(_SUBTYPE)
_PAGEREQTYPE = _descriptor.EnumDescriptor(
  name='PageReqType',
  full_name='ideacrawler.PageReqType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1612,
  serialized_end=1644,
)
_sym_db.RegisterEnumDescriptor(_PAGEREQTYPE)

PageReqType = enum_type_wrapper.EnumTypeWrapper(_PAGEREQTYPE)
SEQNUM = 0
DATETIME = 1
GET = 0
HEAD = 1



_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='ideacrawler.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ideacrawler.Status.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='ideacrawler.Status.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=99,
  serialized_end=139,
)


_KVP = _descriptor.Descriptor(
  name='KVP',
  full_name='ideacrawler.KVP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ideacrawler.KVP.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ideacrawler.KVP.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=141,
  serialized_end=174,
)


_DOMAINOPT = _descriptor.Descriptor(
  name='DomainOpt',
  full_name='ideacrawler.DomainOpt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seedUrl', full_name='ideacrawler.DomainOpt.seedUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minDelay', full_name='ideacrawler.DomainOpt.minDelay', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxDelay', full_name='ideacrawler.DomainOpt.maxDelay', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noFollow', full_name='ideacrawler.DomainOpt.noFollow', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callbackUrlRegexp', full_name='ideacrawler.DomainOpt.callbackUrlRegexp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='followUrlRegexp', full_name='ideacrawler.DomainOpt.followUrlRegexp', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxConcurrentRequests', full_name='ideacrawler.DomainOpt.maxConcurrentRequests', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='useragent', full_name='ideacrawler.DomainOpt.useragent', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='impolite', full_name='ideacrawler.DomainOpt.impolite', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth', full_name='ideacrawler.DomainOpt.depth', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat', full_name='ideacrawler.DomainOpt.repeat', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='ideacrawler.DomainOpt.frequency', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firstrun', full_name='ideacrawler.DomainOpt.firstrun', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callbackXpathMatch', full_name='ideacrawler.DomainOpt.callbackXpathMatch', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callbackXpathRegexp', full_name='ideacrawler.DomainOpt.callbackXpathRegexp', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unused16', full_name='ideacrawler.DomainOpt.unused16', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='followOtherDomains', full_name='ideacrawler.DomainOpt.followOtherDomains', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keepDomains', full_name='ideacrawler.DomainOpt.keepDomains', index=17,
      number=18, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropDomains', full_name='ideacrawler.DomainOpt.dropDomains', index=18,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domainDropPriority', full_name='ideacrawler.DomainOpt.domainDropPriority', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unsafeNormalizeURL', full_name='ideacrawler.DomainOpt.unsafeNormalizeURL', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login', full_name='ideacrawler.DomainOpt.login', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginUsingSelenium', full_name='ideacrawler.DomainOpt.loginUsingSelenium', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginUrl', full_name='ideacrawler.DomainOpt.loginUrl', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginPayload', full_name='ideacrawler.DomainOpt.loginPayload', index=24,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginParseFields', full_name='ideacrawler.DomainOpt.loginParseFields', index=25,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginParseXpath', full_name='ideacrawler.DomainOpt.loginParseXpath', index=26,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginSuccessCheck', full_name='ideacrawler.DomainOpt.loginSuccessCheck', index=27,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkLoginAfterEachPage', full_name='ideacrawler.DomainOpt.checkLoginAfterEachPage', index=28,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unused', full_name='ideacrawler.DomainOpt.unused', index=29,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chrome', full_name='ideacrawler.DomainOpt.chrome', index=30,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chromeBinary', full_name='ideacrawler.DomainOpt.chromeBinary', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domLoadTime', full_name='ideacrawler.DomainOpt.domLoadTime', index=32,
      number=33, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='networkIface', full_name='ideacrawler.DomainOpt.networkIface', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cancelOnDisconnect', full_name='ideacrawler.DomainOpt.cancelOnDisconnect', index=34,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkContent', full_name='ideacrawler.DomainOpt.checkContent', index=35,
      number=36, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=177,
  serialized_end=1134,
)


_SUBSCRIPTION = _descriptor.Descriptor(
  name='Subscription',
  full_name='ideacrawler.Subscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subcode', full_name='ideacrawler.Subscription.subcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domainname', full_name='ideacrawler.Subscription.domainname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='ideacrawler.Subscription.subtype', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqnum', full_name='ideacrawler.Subscription.seqnum', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='ideacrawler.Subscription.datetime', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1137,
  serialized_end=1289,
)


_PAGEREQUEST = _descriptor.Descriptor(
  name='PageRequest',
  full_name='ideacrawler.PageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sub', full_name='ideacrawler.PageRequest.sub', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reqtype', full_name='ideacrawler.PageRequest.reqtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='ideacrawler.PageRequest.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metaStr', full_name='ideacrawler.PageRequest.metaStr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1291,
  serialized_end=1417,
)


_PAGEHTML = _descriptor.Descriptor(
  name='PageHTML',
  full_name='ideacrawler.PageHTML',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ideacrawler.PageHTML.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='ideacrawler.PageHTML.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub', full_name='ideacrawler.PageHTML.sub', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='ideacrawler.PageHTML.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='httpstatuscode', full_name='ideacrawler.PageHTML.httpstatuscode', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='ideacrawler.PageHTML.content', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metaStr', full_name='ideacrawler.PageHTML.metaStr', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1420,
  serialized_end=1573,
)

_DOMAINOPT.fields_by_name['frequency'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_DOMAINOPT.fields_by_name['firstrun'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DOMAINOPT.fields_by_name['callbackXpathMatch'].message_type = _KVP
_DOMAINOPT.fields_by_name['callbackXpathRegexp'].message_type = _KVP
_DOMAINOPT.fields_by_name['loginPayload'].message_type = _KVP
_DOMAINOPT.fields_by_name['loginParseXpath'].message_type = _KVP
_DOMAINOPT.fields_by_name['loginSuccessCheck'].message_type = _KVP
_SUBSCRIPTION.fields_by_name['subtype'].enum_type = _SUBTYPE
_SUBSCRIPTION.fields_by_name['datetime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PAGEREQUEST.fields_by_name['sub'].message_type = _SUBSCRIPTION
_PAGEREQUEST.fields_by_name['reqtype'].enum_type = _PAGEREQTYPE
_PAGEHTML.fields_by_name['sub'].message_type = _SUBSCRIPTION
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['KVP'] = _KVP
DESCRIPTOR.message_types_by_name['DomainOpt'] = _DOMAINOPT
DESCRIPTOR.message_types_by_name['Subscription'] = _SUBSCRIPTION
DESCRIPTOR.message_types_by_name['PageRequest'] = _PAGEREQUEST
DESCRIPTOR.message_types_by_name['PageHTML'] = _PAGEHTML
DESCRIPTOR.enum_types_by_name['SubType'] = _SUBTYPE
DESCRIPTOR.enum_types_by_name['PageReqType'] = _PAGEREQTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'ideacrawler_pb2'
  # @@protoc_insertion_point(class_scope:ideacrawler.Status)
  ))
_sym_db.RegisterMessage(Status)

KVP = _reflection.GeneratedProtocolMessageType('KVP', (_message.Message,), dict(
  DESCRIPTOR = _KVP,
  __module__ = 'ideacrawler_pb2'
  # @@protoc_insertion_point(class_scope:ideacrawler.KVP)
  ))
_sym_db.RegisterMessage(KVP)

DomainOpt = _reflection.GeneratedProtocolMessageType('DomainOpt', (_message.Message,), dict(
  DESCRIPTOR = _DOMAINOPT,
  __module__ = 'ideacrawler_pb2'
  # @@protoc_insertion_point(class_scope:ideacrawler.DomainOpt)
  ))
_sym_db.RegisterMessage(DomainOpt)

Subscription = _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIPTION,
  __module__ = 'ideacrawler_pb2'
  # @@protoc_insertion_point(class_scope:ideacrawler.Subscription)
  ))
_sym_db.RegisterMessage(Subscription)

PageRequest = _reflection.GeneratedProtocolMessageType('PageRequest', (_message.Message,), dict(
  DESCRIPTOR = _PAGEREQUEST,
  __module__ = 'ideacrawler_pb2'
  # @@protoc_insertion_point(class_scope:ideacrawler.PageRequest)
  ))
_sym_db.RegisterMessage(PageRequest)

PageHTML = _reflection.GeneratedProtocolMessageType('PageHTML', (_message.Message,), dict(
  DESCRIPTOR = _PAGEHTML,
  __module__ = 'ideacrawler_pb2'
  # @@protoc_insertion_point(class_scope:ideacrawler.PageHTML)
  ))
_sym_db.RegisterMessage(PageHTML)



_IDEACRAWLER = _descriptor.ServiceDescriptor(
  name='IdeaCrawler',
  full_name='ideacrawler.IdeaCrawler',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1647,
  serialized_end=1859,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddDomainAndListen',
    full_name='ideacrawler.IdeaCrawler.AddDomainAndListen',
    index=0,
    containing_service=None,
    input_type=_DOMAINOPT,
    output_type=_PAGEHTML,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddPages',
    full_name='ideacrawler.IdeaCrawler.AddPages',
    index=1,
    containing_service=None,
    input_type=_PAGEREQUEST,
    output_type=_STATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelJob',
    full_name='ideacrawler.IdeaCrawler.CancelJob',
    index=2,
    containing_service=None,
    input_type=_SUBSCRIPTION,
    output_type=_STATUS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IDEACRAWLER)

DESCRIPTOR.services_by_name['IdeaCrawler'] = _IDEACRAWLER

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class IdeaCrawlerStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.AddDomainAndListen = channel.unary_stream(
          '/ideacrawler.IdeaCrawler/AddDomainAndListen',
          request_serializer=DomainOpt.SerializeToString,
          response_deserializer=PageHTML.FromString,
          )
      self.AddPages = channel.stream_unary(
          '/ideacrawler.IdeaCrawler/AddPages',
          request_serializer=PageRequest.SerializeToString,
          response_deserializer=Status.FromString,
          )
      self.CancelJob = channel.unary_unary(
          '/ideacrawler.IdeaCrawler/CancelJob',
          request_serializer=Subscription.SerializeToString,
          response_deserializer=Status.FromString,
          )


  class IdeaCrawlerServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def AddDomainAndListen(self, request, context):
      """rpc AddDomain(DomainOpt) returns (Subscription) {}
      rpc AddDomains(stream DomainOpt) returns (stream Subscription) {}
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def AddPages(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def CancelJob(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_IdeaCrawlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'AddDomainAndListen': grpc.unary_stream_rpc_method_handler(
            servicer.AddDomainAndListen,
            request_deserializer=DomainOpt.FromString,
            response_serializer=PageHTML.SerializeToString,
        ),
        'AddPages': grpc.stream_unary_rpc_method_handler(
            servicer.AddPages,
            request_deserializer=PageRequest.FromString,
            response_serializer=Status.SerializeToString,
        ),
        'CancelJob': grpc.unary_unary_rpc_method_handler(
            servicer.CancelJob,
            request_deserializer=Subscription.FromString,
            response_serializer=Status.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ideacrawler.IdeaCrawler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaIdeaCrawlerServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def AddDomainAndListen(self, request, context):
      """rpc AddDomain(DomainOpt) returns (Subscription) {}
      rpc AddDomains(stream DomainOpt) returns (stream Subscription) {}
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def AddPages(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def CancelJob(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaIdeaCrawlerStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def AddDomainAndListen(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """rpc AddDomain(DomainOpt) returns (Subscription) {}
      rpc AddDomains(stream DomainOpt) returns (stream Subscription) {}
      """
      raise NotImplementedError()
    def AddPages(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    AddPages.future = None
    def CancelJob(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    CancelJob.future = None


  def beta_create_IdeaCrawler_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('ideacrawler.IdeaCrawler', 'AddDomainAndListen'): DomainOpt.FromString,
      ('ideacrawler.IdeaCrawler', 'AddPages'): PageRequest.FromString,
      ('ideacrawler.IdeaCrawler', 'CancelJob'): Subscription.FromString,
    }
    response_serializers = {
      ('ideacrawler.IdeaCrawler', 'AddDomainAndListen'): PageHTML.SerializeToString,
      ('ideacrawler.IdeaCrawler', 'AddPages'): Status.SerializeToString,
      ('ideacrawler.IdeaCrawler', 'CancelJob'): Status.SerializeToString,
    }
    method_implementations = {
      ('ideacrawler.IdeaCrawler', 'AddDomainAndListen'): face_utilities.unary_stream_inline(servicer.AddDomainAndListen),
      ('ideacrawler.IdeaCrawler', 'AddPages'): face_utilities.stream_unary_inline(servicer.AddPages),
      ('ideacrawler.IdeaCrawler', 'CancelJob'): face_utilities.unary_unary_inline(servicer.CancelJob),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_IdeaCrawler_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('ideacrawler.IdeaCrawler', 'AddDomainAndListen'): DomainOpt.SerializeToString,
      ('ideacrawler.IdeaCrawler', 'AddPages'): PageRequest.SerializeToString,
      ('ideacrawler.IdeaCrawler', 'CancelJob'): Subscription.SerializeToString,
    }
    response_deserializers = {
      ('ideacrawler.IdeaCrawler', 'AddDomainAndListen'): PageHTML.FromString,
      ('ideacrawler.IdeaCrawler', 'AddPages'): Status.FromString,
      ('ideacrawler.IdeaCrawler', 'CancelJob'): Status.FromString,
    }
    cardinalities = {
      'AddDomainAndListen': cardinality.Cardinality.UNARY_STREAM,
      'AddPages': cardinality.Cardinality.STREAM_UNARY,
      'CancelJob': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'ideacrawler.IdeaCrawler', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
