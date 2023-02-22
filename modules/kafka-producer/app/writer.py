import grpc
import location_pb2
import location_pb2_grpc

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:30020")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    latitude=12.6720302007315,
    longitude=103.00302026320003
)

response = stub.Create(location)
