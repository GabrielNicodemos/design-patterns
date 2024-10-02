from abc import ABC, abstractmethod

# Interface básica (comportamento principal)
class Person(ABC):
    @abstractmethod
    def dress(self):
        pass

# Comportamento básico
class BasicPerson(Person):
    def dress(self):
        return "Person is dressed in basic clothing."

# Decorator abstrato
class ClothingDecorator(Person):
    def __init__(self, person: Person):
        self._person = person

    @abstractmethod
    def dress(self):
        pass

# Implementações concretas dos decoradores
class SweaterDecorator(ClothingDecorator):
    def dress(self):
        return f"{self._person.dress()} + a sweater"

class CoatDecorator(ClothingDecorator):
    def dress(self):
        return f"{self._person.dress()} + a coat"

class RaincoatDecorator(ClothingDecorator):
    def dress(self):
        return f"{self._person.dress()} + a raincoat"

# Uso
if __name__ == "__main__":
    # Pessoa básica
    person = BasicPerson()
    print(person.dress())  # Output: Person is dressed in basic clothing.

    # Vestindo um suéter
    person_with_sweater = SweaterDecorator(person)
    print(person_with_sweater.dress())  # Output: Person is dressed in basic clothing. + a sweater

    # Vestindo um suéter e um casaco
    person_with_sweater_and_coat = CoatDecorator(person_with_sweater)
    print(person_with_sweater_and_coat.dress())  # Output: Person is dressed in basic clothing. + a sweater + a coat

    # Vestindo um suéter, casaco e capa de chuva
    fully_dressed_person = RaincoatDecorator(person_with_sweater_and_coat)
    print(fully_dressed_person.dress())  # Output: Person is dressed in basic clothing. + a sweater + a coat + a raincoat