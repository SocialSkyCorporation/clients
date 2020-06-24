# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from client import client_pb2 as client_dot_client__pb2


class ClientStub(object):
    """Client is the micro client interface
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/go.micro.client.Client/Call',
                request_serializer=client_dot_client__pb2.Request.SerializeToString,
                response_deserializer=client_dot_client__pb2.Response.FromString,
                )
        self.Stream = channel.stream_stream(
                '/go.micro.client.Client/Stream',
                request_serializer=client_dot_client__pb2.Request.SerializeToString,
                response_deserializer=client_dot_client__pb2.Response.FromString,
                )
        self.Publish = channel.unary_unary(
                '/go.micro.client.Client/Publish',
                request_serializer=client_dot_client__pb2.Message.SerializeToString,
                response_deserializer=client_dot_client__pb2.Message.FromString,
                )


class ClientServicer(object):
    """Client is the micro client interface
    """

    def Call(self, request, context):
        """Call allows a single request to be made
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream(self, request_iterator, context):
        """Stream is a bidirectional stream
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publish(self, request, context):
        """Publish publishes a message and returns an empty Message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=client_dot_client__pb2.Request.FromString,
                    response_serializer=client_dot_client__pb2.Response.SerializeToString,
            ),
            'Stream': grpc.stream_stream_rpc_method_handler(
                    servicer.Stream,
                    request_deserializer=client_dot_client__pb2.Request.FromString,
                    response_serializer=client_dot_client__pb2.Response.SerializeToString,
            ),
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=client_dot_client__pb2.Message.FromString,
                    response_serializer=client_dot_client__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'go.micro.client.Client', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Client(object):
    """Client is the micro client interface
    """

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.client.Client/Call',
            client_dot_client__pb2.Request.SerializeToString,
            client_dot_client__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/go.micro.client.Client/Stream',
            client_dot_client__pb2.Request.SerializeToString,
            client_dot_client__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.client.Client/Publish',
            client_dot_client__pb2.Message.SerializeToString,
            client_dot_client__pb2.Message.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
