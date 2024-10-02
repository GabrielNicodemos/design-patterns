class Government:
    _instance = None  # Atributo de classe que armazena a única instância

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Verifica se a instância já foi criada
            cls._instance = super(Government, cls).__new__(cls)  # Cria a nova instância
            cls._instance.name = kwargs.get('name', 'Governo Desconhecido')
            cls._instance.leaders = []  # Inicializa a lista de líderes
        return cls._instance  # Retorna a instância única

    def add_leader(self, leader_name):
        """Adiciona um líder ao governo."""
        self.leaders.append(leader_name)

    def get_government_info(self):
        """Retorna informações sobre o governo."""
        return f"{self.name} com líderes: {', '.join(self.leaders)}"

# Exemplo de uso do Singleton
if __name__ == "__main__":
    # Criação da primeira instância do governo
    government1 = Government(name='Governo do Brasil')
    government1.add_leader('Presidente XPTO')

    # Tentativa de criar uma segunda instância
    government2 = Government(name='Governo do Brasil')
    government2.add_leader('Presidente B')

    # Exibindo informações
    print(government1.get_government_info())  # Saída: Governo do Brasil com líderes: Presidente A, Presidente B
    print(government2.get_government_info())  # Saída: Governo do Brasil com líderes: Presidente A, Presidente B

    # Verificando se ambas as variáveis apontam para a mesma instância
    print(government1 is government2)  # Saída: True