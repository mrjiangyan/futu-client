# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_GetOwnerPlate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_GetOwnerPlate.proto',
  package='Qot_GetOwnerPlate',
  syntax='proto2',
  serialized_pb=_b('\n\x17Qot_GetOwnerPlate.proto\x12\x11Qot_GetOwnerPlate\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"1\n\x03\x43\x32S\x12*\n\x0csecurityList\x18\x01 \x03(\x0b\x32\x14.Qot_Common.Security\"x\n\x12SecurityOwnerPlate\x12&\n\x08security\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\x12\x0c\n\x04name\x18\x03 \x01(\t\x12,\n\rplateInfoList\x18\x02 \x03(\x0b\x32\x15.Qot_Common.PlateInfo\"D\n\x03S2C\x12=\n\x0eownerPlateList\x18\x01 \x03(\x0b\x32%.Qot_GetOwnerPlate.SecurityOwnerPlate\".\n\x07Request\x12#\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x16.Qot_GetOwnerPlate.C2S\"g\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12#\n\x03s2c\x18\x04 \x01(\x0b\x32\x16.Qot_GetOwnerPlate.S2CBG\n\x13\x63om.futu.openapi.pbZ0github.com/futuopen/ftapi4go/pb/qotgetownerplate')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_GetOwnerPlate.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='securityList', full_name='Qot_GetOwnerPlate.C2S.securityList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=127,
)


_SECURITYOWNERPLATE = _descriptor.Descriptor(
  name='SecurityOwnerPlate',
  full_name='Qot_GetOwnerPlate.SecurityOwnerPlate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_GetOwnerPlate.SecurityOwnerPlate.security', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Qot_GetOwnerPlate.SecurityOwnerPlate.name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plateInfoList', full_name='Qot_GetOwnerPlate.SecurityOwnerPlate.plateInfoList', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=249,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_GetOwnerPlate.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ownerPlateList', full_name='Qot_GetOwnerPlate.S2C.ownerPlateList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=319,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_GetOwnerPlate.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_GetOwnerPlate.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=367,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_GetOwnerPlate.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_GetOwnerPlate.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_GetOwnerPlate.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_GetOwnerPlate.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_GetOwnerPlate.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=472,
)

_C2S.fields_by_name['securityList'].message_type = Qot__Common__pb2._SECURITY
_SECURITYOWNERPLATE.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_SECURITYOWNERPLATE.fields_by_name['plateInfoList'].message_type = Qot__Common__pb2._PLATEINFO
_S2C.fields_by_name['ownerPlateList'].message_type = _SECURITYOWNERPLATE
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['SecurityOwnerPlate'] = _SECURITYOWNERPLATE
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_GetOwnerPlate_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOwnerPlate.C2S)
  ))
_sym_db.RegisterMessage(C2S)

SecurityOwnerPlate = _reflection.GeneratedProtocolMessageType('SecurityOwnerPlate', (_message.Message,), dict(
  DESCRIPTOR = _SECURITYOWNERPLATE,
  __module__ = 'Qot_GetOwnerPlate_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOwnerPlate.SecurityOwnerPlate)
  ))
_sym_db.RegisterMessage(SecurityOwnerPlate)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_GetOwnerPlate_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOwnerPlate.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_GetOwnerPlate_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOwnerPlate.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_GetOwnerPlate_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOwnerPlate.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pbZ0github.com/futuopen/ftapi4go/pb/qotgetownerplate'))
# @@protoc_insertion_point(module_scope)
