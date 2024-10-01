from abc import ABC, abstractmethod

# Interface da Estratégia
class DiscountsStrategy(ABC):
    @abstractmethod
    def generate_discount(self, value_sales: float, discont: int) -> str:
        pass

# Estratégia disconto por cupom
class CouponStrategy(DiscountsStrategy):
    def generate_discount(self, value_sales: float, discont: int) -> str:
        calc = value_sales - (value_sales * (discont/100))
        return f"Sua compra vai sair por {calc} com desconto de {discont}%."

# Estratégia disconto por sócio
class PartnerStrategy(DiscountsStrategy):
    def generate_discount(self, value_sales: float, discont: int) -> str:

        partner = "Plus"
        if discont > 10:
            partner = "Premium"
        calc = value_sales - (value_sales * (discont/100))
        return f"Sua compra vai sair por {calc} com desconto de {discont}%. Parabéns você é um parceiro {partner}"

# Estratégia disconto por indicação
class IndicationStrategy(DiscountsStrategy):
    def generate_discount(self, value_sales: float, discont: int) -> str:
        calc = value_sales - (value_sales * (discont/100))

        discount_for_indication = value_sales * (discont/100)
        return f"Sua compra vai sair por {calc} com desconto de {discont}%. Quem indicou ganhar R$ {discount_for_indication}."

# Contexto
class Discount:
    def __init__(self, strategy: DiscountsStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountsStrategy):
        self.strategy = strategy

    def generate_discount(self, value_sales: float, discont: int) -> str:
        return self.strategy.generate_discount(value_sales, discont)


# Cliente
if __name__ == "__main__":
    discount = Discount(CouponStrategy())
    print(discount.generate_discount(400.00, 10))

    discount.set_strategy(PartnerStrategy())
    print(discount.generate_discount(400.00, 10))

    discount.set_strategy(IndicationStrategy())
    print(discount.generate_discount(400.00, 10))