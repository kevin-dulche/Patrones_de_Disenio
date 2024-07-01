def client_vehicle_code(factory, vehicle_type: str):
    vehicle = factory.get_vehicle(vehicle_type)
    print(vehicle.deliver())