# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: runtime/runtime.proto for package 'go.micro.runtime'

require 'grpc'
require 'runtime/runtime_pb'

module Go
  module Micro
    module Runtime
      module Runtime
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.runtime.Runtime'

          rpc :Create, CreateRequest, CreateResponse
          rpc :Read, ReadRequest, ReadResponse
          rpc :Delete, DeleteRequest, DeleteResponse
          rpc :Update, UpdateRequest, UpdateResponse
          rpc :Logs, LogsRequest, stream(LogRecord)
        end

        Stub = Service.rpc_stub_class
      end
    end
  end
end
