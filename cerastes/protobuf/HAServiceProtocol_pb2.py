# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='HAServiceProtocol.proto',
  package='hadoop.common',
  serialized_pb='\n\x17HAServiceProtocol.proto\x12\rhadoop.common\"R\n\x1dHAStateChangeRequestInfoProto\x12\x31\n\treqSource\x18\x01 \x02(\x0e\x32\x1e.hadoop.common.HARequestSource\"\x1b\n\x19MonitorHealthRequestProto\"\x1c\n\x1aMonitorHealthResponseProto\"_\n\x1eTransitionToActiveRequestProto\x12=\n\x07reqInfo\x18\x01 \x02(\x0b\x32,.hadoop.common.HAStateChangeRequestInfoProto\"!\n\x1fTransitionToActiveResponseProto\"`\n\x1fTransitionToStandbyRequestProto\x12=\n\x07reqInfo\x18\x01 \x02(\x0b\x32,.hadoop.common.HAStateChangeRequestInfoProto\"\"\n TransitionToStandbyResponseProto\"\x1e\n\x1cGetServiceStatusRequestProto\"\x87\x01\n\x1dGetServiceStatusResponseProto\x12\x31\n\x05state\x18\x01 \x02(\x0e\x32\".hadoop.common.HAServiceStateProto\x12\x1b\n\x13readyToBecomeActive\x18\x02 \x01(\x08\x12\x16\n\x0enotReadyReason\x18\x03 \x01(\t*@\n\x13HAServiceStateProto\x12\x10\n\x0cINITIALIZING\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0b\n\x07STANDBY\x10\x02*W\n\x0fHARequestSource\x12\x13\n\x0fREQUEST_BY_USER\x10\x00\x12\x1a\n\x16REQUEST_BY_USER_FORCED\x10\x01\x12\x13\n\x0fREQUEST_BY_ZKFC\x10\x02\x32\xdc\x03\n\x18HAServiceProtocolService\x12\x64\n\rmonitorHealth\x12(.hadoop.common.MonitorHealthRequestProto\x1a).hadoop.common.MonitorHealthResponseProto\x12s\n\x12transitionToActive\x12-.hadoop.common.TransitionToActiveRequestProto\x1a..hadoop.common.TransitionToActiveResponseProto\x12v\n\x13transitionToStandby\x12..hadoop.common.TransitionToStandbyRequestProto\x1a/.hadoop.common.TransitionToStandbyResponseProto\x12m\n\x10getServiceStatus\x12+.hadoop.common.GetServiceStatusRequestProto\x1a,.hadoop.common.GetServiceStatusResponseProtoB>\n\x1aorg.apache.hadoop.ha.protoB\x17HAServiceProtocolProtos\x88\x01\x01\x90\x01\x01\xa0\x01\x01')

_HASERVICESTATEPROTO = descriptor.EnumDescriptor(
  name='HAServiceStateProto',
  full_name='hadoop.common.HAServiceStateProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='INITIALIZING', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STANDBY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=621,
  serialized_end=685,
)


_HAREQUESTSOURCE = descriptor.EnumDescriptor(
  name='HARequestSource',
  full_name='hadoop.common.HARequestSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='REQUEST_BY_USER', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='REQUEST_BY_USER_FORCED', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='REQUEST_BY_ZKFC', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=687,
  serialized_end=774,
)


INITIALIZING = 0
ACTIVE = 1
STANDBY = 2
REQUEST_BY_USER = 0
REQUEST_BY_USER_FORCED = 1
REQUEST_BY_ZKFC = 2



_HASTATECHANGEREQUESTINFOPROTO = descriptor.Descriptor(
  name='HAStateChangeRequestInfoProto',
  full_name='hadoop.common.HAStateChangeRequestInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reqSource', full_name='hadoop.common.HAStateChangeRequestInfoProto.reqSource', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=42,
  serialized_end=124,
)


_MONITORHEALTHREQUESTPROTO = descriptor.Descriptor(
  name='MonitorHealthRequestProto',
  full_name='hadoop.common.MonitorHealthRequestProto',
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
  extension_ranges=[],
  serialized_start=126,
  serialized_end=153,
)


_MONITORHEALTHRESPONSEPROTO = descriptor.Descriptor(
  name='MonitorHealthResponseProto',
  full_name='hadoop.common.MonitorHealthResponseProto',
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
  extension_ranges=[],
  serialized_start=155,
  serialized_end=183,
)


_TRANSITIONTOACTIVEREQUESTPROTO = descriptor.Descriptor(
  name='TransitionToActiveRequestProto',
  full_name='hadoop.common.TransitionToActiveRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reqInfo', full_name='hadoop.common.TransitionToActiveRequestProto.reqInfo', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=185,
  serialized_end=280,
)


_TRANSITIONTOACTIVERESPONSEPROTO = descriptor.Descriptor(
  name='TransitionToActiveResponseProto',
  full_name='hadoop.common.TransitionToActiveResponseProto',
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
  extension_ranges=[],
  serialized_start=282,
  serialized_end=315,
)


_TRANSITIONTOSTANDBYREQUESTPROTO = descriptor.Descriptor(
  name='TransitionToStandbyRequestProto',
  full_name='hadoop.common.TransitionToStandbyRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reqInfo', full_name='hadoop.common.TransitionToStandbyRequestProto.reqInfo', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=317,
  serialized_end=413,
)


_TRANSITIONTOSTANDBYRESPONSEPROTO = descriptor.Descriptor(
  name='TransitionToStandbyResponseProto',
  full_name='hadoop.common.TransitionToStandbyResponseProto',
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
  extension_ranges=[],
  serialized_start=415,
  serialized_end=449,
)


_GETSERVICESTATUSREQUESTPROTO = descriptor.Descriptor(
  name='GetServiceStatusRequestProto',
  full_name='hadoop.common.GetServiceStatusRequestProto',
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
  extension_ranges=[],
  serialized_start=451,
  serialized_end=481,
)


_GETSERVICESTATUSRESPONSEPROTO = descriptor.Descriptor(
  name='GetServiceStatusResponseProto',
  full_name='hadoop.common.GetServiceStatusResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='state', full_name='hadoop.common.GetServiceStatusResponseProto.state', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='readyToBecomeActive', full_name='hadoop.common.GetServiceStatusResponseProto.readyToBecomeActive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='notReadyReason', full_name='hadoop.common.GetServiceStatusResponseProto.notReadyReason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=484,
  serialized_end=619,
)

_HASTATECHANGEREQUESTINFOPROTO.fields_by_name['reqSource'].enum_type = _HAREQUESTSOURCE
_TRANSITIONTOACTIVEREQUESTPROTO.fields_by_name['reqInfo'].message_type = _HASTATECHANGEREQUESTINFOPROTO
_TRANSITIONTOSTANDBYREQUESTPROTO.fields_by_name['reqInfo'].message_type = _HASTATECHANGEREQUESTINFOPROTO
_GETSERVICESTATUSRESPONSEPROTO.fields_by_name['state'].enum_type = _HASERVICESTATEPROTO
DESCRIPTOR.message_types_by_name['HAStateChangeRequestInfoProto'] = _HASTATECHANGEREQUESTINFOPROTO
DESCRIPTOR.message_types_by_name['MonitorHealthRequestProto'] = _MONITORHEALTHREQUESTPROTO
DESCRIPTOR.message_types_by_name['MonitorHealthResponseProto'] = _MONITORHEALTHRESPONSEPROTO
DESCRIPTOR.message_types_by_name['TransitionToActiveRequestProto'] = _TRANSITIONTOACTIVEREQUESTPROTO
DESCRIPTOR.message_types_by_name['TransitionToActiveResponseProto'] = _TRANSITIONTOACTIVERESPONSEPROTO
DESCRIPTOR.message_types_by_name['TransitionToStandbyRequestProto'] = _TRANSITIONTOSTANDBYREQUESTPROTO
DESCRIPTOR.message_types_by_name['TransitionToStandbyResponseProto'] = _TRANSITIONTOSTANDBYRESPONSEPROTO
DESCRIPTOR.message_types_by_name['GetServiceStatusRequestProto'] = _GETSERVICESTATUSREQUESTPROTO
DESCRIPTOR.message_types_by_name['GetServiceStatusResponseProto'] = _GETSERVICESTATUSRESPONSEPROTO

class HAStateChangeRequestInfoProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HASTATECHANGEREQUESTINFOPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.HAStateChangeRequestInfoProto)

class MonitorHealthRequestProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MONITORHEALTHREQUESTPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.MonitorHealthRequestProto)

class MonitorHealthResponseProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MONITORHEALTHRESPONSEPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.MonitorHealthResponseProto)

class TransitionToActiveRequestProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSITIONTOACTIVEREQUESTPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.TransitionToActiveRequestProto)

class TransitionToActiveResponseProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSITIONTOACTIVERESPONSEPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.TransitionToActiveResponseProto)

class TransitionToStandbyRequestProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSITIONTOSTANDBYREQUESTPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.TransitionToStandbyRequestProto)

class TransitionToStandbyResponseProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSITIONTOSTANDBYRESPONSEPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.TransitionToStandbyResponseProto)

class GetServiceStatusRequestProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSERVICESTATUSREQUESTPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.GetServiceStatusRequestProto)

class GetServiceStatusResponseProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSERVICESTATUSRESPONSEPROTO
  
  # @@protoc_insertion_point(class_scope:hadoop.common.GetServiceStatusResponseProto)


_HASERVICEPROTOCOLSERVICE = descriptor.ServiceDescriptor(
  name='HAServiceProtocolService',
  full_name='hadoop.common.HAServiceProtocolService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=777,
  serialized_end=1253,
  methods=[
  descriptor.MethodDescriptor(
    name='monitorHealth',
    full_name='hadoop.common.HAServiceProtocolService.monitorHealth',
    index=0,
    containing_service=None,
    input_type=_MONITORHEALTHREQUESTPROTO,
    output_type=_MONITORHEALTHRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='transitionToActive',
    full_name='hadoop.common.HAServiceProtocolService.transitionToActive',
    index=1,
    containing_service=None,
    input_type=_TRANSITIONTOACTIVEREQUESTPROTO,
    output_type=_TRANSITIONTOACTIVERESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='transitionToStandby',
    full_name='hadoop.common.HAServiceProtocolService.transitionToStandby',
    index=2,
    containing_service=None,
    input_type=_TRANSITIONTOSTANDBYREQUESTPROTO,
    output_type=_TRANSITIONTOSTANDBYRESPONSEPROTO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='getServiceStatus',
    full_name='hadoop.common.HAServiceProtocolService.getServiceStatus',
    index=3,
    containing_service=None,
    input_type=_GETSERVICESTATUSREQUESTPROTO,
    output_type=_GETSERVICESTATUSRESPONSEPROTO,
    options=None,
  ),
])

class HAServiceProtocolService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _HASERVICEPROTOCOLSERVICE
class HAServiceProtocolService_Stub(HAServiceProtocolService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _HASERVICEPROTOCOLSERVICE

# @@protoc_insertion_point(module_scope)
