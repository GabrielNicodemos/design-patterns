class EuropeanElectricalSocket:
    def charge(self, charge: bool):
        pass

class BrazilianElectricalSocket:
    def charge(self, charge: bool):
        print(f"Charging Smartphone: {charge} - Brazilian Electrical Socket")

class AfricanElectricalSocket:
    def charge(self, charge: bool):
        print(f"Charging Smartphone: {charge} - African Electrical Socket")

class BrazilianToEuropeanAdapter(EuropeanElectricalSocket):
    def __init__(self, brazilian_electrical_socket: BrazilianElectricalSocket):
        self.brazilian_electrical_socket = brazilian_electrical_socket

    def charge(self, charge: bool):
        self.brazilian_electrical_socket.charge(charge)

class AfricanToEuropeanAdapter(EuropeanElectricalSocket):
    def __init__(self, african_electrical_socket: AfricanElectricalSocket):
        self.african_electrical_socket = african_electrical_socket

    def charge(self, charge: bool):
        self.african_electrical_socket.charge(charge)


if __name__ == "__main__":
    brazilian_electrical_socket = BrazilianElectricalSocket()
    adapter = BrazilianToEuropeanAdapter(brazilian_electrical_socket)

    adapter.charge(True)  # Output: Charging Smartphone: True

    african_electrical_socket = AfricanElectricalSocket()
    adapter = AfricanToEuropeanAdapter(african_electrical_socket)

    adapter.charge(True)  # Output: Charging Smartphone: True