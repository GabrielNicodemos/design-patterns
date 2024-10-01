from abc import ABC, abstractmethod

# Interface da Estratégia
class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start: str, end: str) -> str:
        pass

# Estratégia Concreta para Rodovias
class HighwayStrategy(RouteStrategy):
    def build_route(self, start: str, end: str) -> str:
        return f"Construindo rota de rodovia de {start} a {end}."

# Estratégia Concreta para Caminhadas
class WalkingStrategy(RouteStrategy):
    def build_route(self, start: str, end: str) -> str:
        return f"Construindo rota de caminhada de {start} a {end}."

# Estratégia Concreta para Transporte Público
class PublicTransportStrategy(RouteStrategy):
    def build_route(self, start: str, end: str) -> str:
        return f"Construindo rota de transporte público de {start} a {end}."

# Mudando para a estratégia de ciclistas
    navigator.set_strategy(BicyclingStrategy())
    print(navigator.build_route("Casa", "Praia"))

# Contexto
class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self.strategy = strategy

    def build_route(self, start: str, end: str) -> str:
        return self.strategy.build_route(start, end)

# Cliente
if __name__ == "__main__":
    # Criando um navegador e configurando uma estratégia
    navigator = Navigator(HighwayStrategy())
    print(navigator.build_route("Casa", "Trabalho"))

    # Mudando para a estratégia de caminhada
    navigator.set_strategy(WalkingStrategy())
    print(navigator.build_route("Casa", "Parque"))

    # Mudando para transporte público
    navigator.set_strategy(PublicTransportStrategy())
    print(navigator.build_route("Casa", "Shopping"))

    # Mudando para a estratégia de ciclistas
    # navigator.set_strategy(BicyclingStrategy())
    # print(navigator.build_route("Casa", "Praia"))