import grpc
import UserAddresses_pb2
import UserAddresses_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = UserAddresses_pb2_grpc.UserAddressesStub(channel)
  response = stub.List(UserAddresses_pb2.UserRequest(id=1))
  print(response)


if __name__ == '__main__':
  run()