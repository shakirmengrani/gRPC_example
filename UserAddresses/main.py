from model import *
from concurrent import futures
import time
import grpc
import UserAddresses_pb2
import UserAddresses_pb2_grpc

class UserAddresses(UserAddresses_pb2_grpc.UserAddressesServicer):

    def List(self, request, context):
        users = db.query(User).filter(User.id==request.id).first()
        addr = []
        for addr_row in users.addresses:
            addr.append(UserAddresses_pb2.UserResponse.Address(location=addr_row.location))
        # time.sleep(15)
        return UserAddresses_pb2.UserResponse(name=users.name, email=users.email, addresses=addr)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    UserAddresses_pb2_grpc.add_UserAddressesServicer_to_server(UserAddresses(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()