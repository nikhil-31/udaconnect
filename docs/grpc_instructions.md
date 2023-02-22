## Instructions to run the GRPC request

1. The proto file is in the path  `./modules/kafka-producer/app/location.proto`, 
2. The grpc server runs on the port `localhost:30012`. The port is exposed as the nodeport from kubernetes
3. The payload to create a new location is
```
{
    "latitude": -122.290883,
    "longitude": 37.55363,
    "person_id": 11
}
```