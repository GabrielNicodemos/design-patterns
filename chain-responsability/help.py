from abc import ABC, abstractmethod

# Classe base para os manipuladores
class Support(ABC):
    def __init__(self, next_support=None):
        self._next_support = next_support

    @abstractmethod
    def handle_order(self, problem):
        pass

    def move_to_next(self, problem):
        if self._next_support:
            return self._next_support.handle_order(problem)
        return "Problema não resolvido"

# Manipulador 1: Voz robótica
class RoboticVoice(Support):
    def handle_order(self, problema):
        print("Voz Robótica: Tentando soluções automáticas...")

        # Tentativa de resolver o problema com soluções padrões
        if problem == "common_problem":
            return "Solução da voz robótica aplicou correções."
        else:
            print("Voz Robótica: Não consegui resolver o problema.")
            return self.move_to_next(problem)

# Manipulador 2: Operador humano
class HumanOperator(Support):
    def handle_order(self, problema):
        print("Operador Humano: Seguindo o protocolo padrão...")
        # Tenta resolver seguindo um manual
        if problem == "intermediate_problem":
            return "Solução aplicada pelo operador humano."
        else:
            print("Operador Humano: Não consigo resolver esse problema.")
            return self.move_to_next(problem)

# Manipulador 3: Engenheiro
class Engineer(Support):
    def handle_order(self, problema):
        print("Engenheiro: Investigando o problema técnico...")
        # Resolve problemas mais técnicos
        if problem == "technical_problem":
            return "Engenheiro: Problema resolvido! Instale o driver no Linux."
        else:
            return self.move_to_next(problem)

# Criação da cadeia de responsabilidade
robotic_voice = RoboticVoice()
human_operator = HumanOperator()
engineer = Engineer()

# Conectar os manipuladores
robotic_voice._next_support = human_operator
human_operator._next_support = engineer

# Simulação do problema
problem = "technical_problem"
result = robotic_voice.handle_order(problem)
print(f"\nResultado final: {result}")