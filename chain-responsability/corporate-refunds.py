from abc import ABC, abstractmethod

# Classe base para os manipuladores
class Corporate(ABC):
    def __init__(self, next_leader=None):
        self._next_leader = next_leader

    @abstractmethod
    def approve_refund(self, value):
        pass

    def next_to_leader(self, value):
        if self._next_leader:
            return self._next_leader.approve_refund(value)
        return "Reembolso não aprovado"

# Manipulador 1: Supervisor
class Supervisor(Corporate):
    def approve_refund(self, value):
        if value and value < 1000:
            return "Reembolso aprovado pelo Supervisor."
        else:
            return self.next_to_leader(value)

# Manipulador 2: Gerente
class Manager(Corporate):
    def approve_refund(self, value):
        if value and value <= 10000:
            return "Reembolso aprovado pelo Gerente."
        else:
            return self.next_to_leader(value)

# Manipulador 3: Diretor
class Director(Corporate):
    def approve_refund(self, value):
        if value and value > 10000:
            return "Reembolso aprovado pelo Diretor."
        else:
            return self.next_to_leader(value)


# Criação da cadeia de responsabilidade
supervisor = Supervisor()
manager = Manager()
director = Director()

# Conectar os manipuladores
supervisor._next_leader = manager
manager._next_leader = director


value = 900
result = supervisor.approve_refund(value)
print(f"\nResultado final: {result}")
# resultado = "Resultado final: Reembolso aprovado pelo Supervisor."

value = 5000
result = supervisor.approve_refund(value)
print(f"\nResultado final: {result}")
# resultado = "Resultado final: Reembolso aprovado pelo Gerente."

value = 13000
result = supervisor.approve_refund(value)
print(f"\nResultado final: {result}")
# resultado = "Resultado final: Reembolso aprovado pelo Diretor."

value = False
result = supervisor.approve_refund(value)
print(f"\nResultado final: {result}")
# resultado = "Reembolso não aprovado"
