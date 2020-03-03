// Code generated by protoc-gen-go. DO NOT EDIT.
// source: github.com/micro/clients/proto/client/client.proto

package go_micro_client

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Request struct {
	Service              string   `protobuf:"bytes,1,opt,name=service,proto3" json:"service,omitempty"`
	Endpoint             string   `protobuf:"bytes,2,opt,name=endpoint,proto3" json:"endpoint,omitempty"`
	ContentType          string   `protobuf:"bytes,3,opt,name=content_type,json=contentType,proto3" json:"content_type,omitempty"`
	Body                 []byte   `protobuf:"bytes,4,opt,name=body,proto3" json:"body,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Request) Reset()         { *m = Request{} }
func (m *Request) String() string { return proto.CompactTextString(m) }
func (*Request) ProtoMessage()    {}
func (*Request) Descriptor() ([]byte, []int) {
	return fileDescriptor_81c8aad97b6341e5, []int{0}
}

func (m *Request) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Request.Unmarshal(m, b)
}
func (m *Request) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Request.Marshal(b, m, deterministic)
}
func (m *Request) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Request.Merge(m, src)
}
func (m *Request) XXX_Size() int {
	return xxx_messageInfo_Request.Size(m)
}
func (m *Request) XXX_DiscardUnknown() {
	xxx_messageInfo_Request.DiscardUnknown(m)
}

var xxx_messageInfo_Request proto.InternalMessageInfo

func (m *Request) GetService() string {
	if m != nil {
		return m.Service
	}
	return ""
}

func (m *Request) GetEndpoint() string {
	if m != nil {
		return m.Endpoint
	}
	return ""
}

func (m *Request) GetContentType() string {
	if m != nil {
		return m.ContentType
	}
	return ""
}

func (m *Request) GetBody() []byte {
	if m != nil {
		return m.Body
	}
	return nil
}

type Response struct {
	Body                 []byte   `protobuf:"bytes,1,opt,name=body,proto3" json:"body,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Response) Reset()         { *m = Response{} }
func (m *Response) String() string { return proto.CompactTextString(m) }
func (*Response) ProtoMessage()    {}
func (*Response) Descriptor() ([]byte, []int) {
	return fileDescriptor_81c8aad97b6341e5, []int{1}
}

func (m *Response) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Response.Unmarshal(m, b)
}
func (m *Response) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Response.Marshal(b, m, deterministic)
}
func (m *Response) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Response.Merge(m, src)
}
func (m *Response) XXX_Size() int {
	return xxx_messageInfo_Response.Size(m)
}
func (m *Response) XXX_DiscardUnknown() {
	xxx_messageInfo_Response.DiscardUnknown(m)
}

var xxx_messageInfo_Response proto.InternalMessageInfo

func (m *Response) GetBody() []byte {
	if m != nil {
		return m.Body
	}
	return nil
}

type Message struct {
	Topic                string   `protobuf:"bytes,1,opt,name=topic,proto3" json:"topic,omitempty"`
	ContentType          string   `protobuf:"bytes,2,opt,name=content_type,json=contentType,proto3" json:"content_type,omitempty"`
	Body                 []byte   `protobuf:"bytes,3,opt,name=body,proto3" json:"body,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Message) Reset()         { *m = Message{} }
func (m *Message) String() string { return proto.CompactTextString(m) }
func (*Message) ProtoMessage()    {}
func (*Message) Descriptor() ([]byte, []int) {
	return fileDescriptor_81c8aad97b6341e5, []int{2}
}

func (m *Message) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Message.Unmarshal(m, b)
}
func (m *Message) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Message.Marshal(b, m, deterministic)
}
func (m *Message) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Message.Merge(m, src)
}
func (m *Message) XXX_Size() int {
	return xxx_messageInfo_Message.Size(m)
}
func (m *Message) XXX_DiscardUnknown() {
	xxx_messageInfo_Message.DiscardUnknown(m)
}

var xxx_messageInfo_Message proto.InternalMessageInfo

func (m *Message) GetTopic() string {
	if m != nil {
		return m.Topic
	}
	return ""
}

func (m *Message) GetContentType() string {
	if m != nil {
		return m.ContentType
	}
	return ""
}

func (m *Message) GetBody() []byte {
	if m != nil {
		return m.Body
	}
	return nil
}

func init() {
	proto.RegisterType((*Request)(nil), "go.micro.client.Request")
	proto.RegisterType((*Response)(nil), "go.micro.client.Response")
	proto.RegisterType((*Message)(nil), "go.micro.client.Message")
}

func init() {
	proto.RegisterFile("github.com/micro/clients/proto/client/client.proto", fileDescriptor_81c8aad97b6341e5)
}

var fileDescriptor_81c8aad97b6341e5 = []byte{
	// 242 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x74, 0x90, 0x31, 0x4f, 0xc3, 0x30,
	0x10, 0x85, 0x49, 0x1b, 0x9a, 0x72, 0x54, 0x42, 0x3a, 0x31, 0x98, 0x0e, 0xa8, 0x64, 0xea, 0xe4,
	0x48, 0x65, 0x66, 0xea, 0xc0, 0xc4, 0x12, 0x21, 0x56, 0xd4, 0xb8, 0xa7, 0x60, 0x29, 0xf5, 0x99,
	0xf8, 0x5a, 0x29, 0xff, 0x1e, 0xc9, 0x49, 0x29, 0x02, 0x3a, 0xd9, 0xef, 0x7d, 0x96, 0xef, 0xdd,
	0x83, 0x55, 0x6d, 0xe5, 0x63, 0x5f, 0x69, 0xc3, 0xbb, 0x62, 0x67, 0x4d, 0xcb, 0x85, 0x69, 0x2c,
	0x39, 0x09, 0x85, 0x6f, 0x59, 0x8e, 0x6a, 0x38, 0x74, 0xf4, 0xf0, 0xa6, 0x66, 0x1d, 0xdf, 0xea,
	0xde, 0xce, 0x0f, 0x90, 0x95, 0xf4, 0xb9, 0xa7, 0x20, 0xa8, 0x20, 0x0b, 0xd4, 0x1e, 0xac, 0x21,
	0x95, 0x2c, 0x92, 0xe5, 0x55, 0x79, 0x94, 0x38, 0x87, 0x29, 0xb9, 0xad, 0x67, 0xeb, 0x44, 0x8d,
	0x22, 0xfa, 0xd6, 0xf8, 0x00, 0x33, 0xc3, 0x4e, 0xc8, 0xc9, 0xbb, 0x74, 0x9e, 0xd4, 0x38, 0xf2,
	0xeb, 0xc1, 0x7b, 0xed, 0x3c, 0x21, 0x42, 0x5a, 0xf1, 0xb6, 0x53, 0xe9, 0x22, 0x59, 0xce, 0xca,
	0x78, 0xcf, 0xef, 0x61, 0x5a, 0x52, 0xf0, 0xec, 0xc2, 0x89, 0x27, 0x3f, 0xf8, 0x1b, 0x64, 0x2f,
	0x14, 0xc2, 0xa6, 0x26, 0xbc, 0x85, 0x4b, 0x61, 0x6f, 0xcd, 0x90, 0xaa, 0x17, 0x7f, 0xe6, 0x8e,
	0xce, 0xcf, 0x1d, 0x9f, 0xfe, 0x5d, 0x3d, 0xc3, 0x64, 0x1d, 0x37, 0xc7, 0x27, 0x48, 0xd7, 0x9b,
	0xa6, 0x41, 0xa5, 0x7f, 0x75, 0xa2, 0x87, 0x42, 0xe6, 0x77, 0xff, 0x90, 0x3e, 0x72, 0x7e, 0x51,
	0x4d, 0x62, 0xa1, 0x8f, 0x5f, 0x01, 0x00, 0x00, 0xff, 0xff, 0xbe, 0x62, 0xb0, 0x8f, 0x86, 0x01,
	0x00, 0x00,
}
