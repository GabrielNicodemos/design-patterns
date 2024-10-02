import logging

class Logger:
    _instance = None  # Atributo de classe para armazenar a instância

    def __new__(cls):
        if cls._instance is None:  # Se a instância não existe
            cls._instance = super(Logger, cls).__new__(cls)  # Cria a instância
            cls._instance.logger = logging.getLogger("MyLogger")  # Cria um logger
            cls._instance.logger.setLevel(logging.DEBUG)  # Define o nível de log

            # Cria um manipulador para escrever logs em um arquivo
            handler = logging.FileHandler("app.log")
            handler.setLevel(logging.DEBUG)

            # Define o formato das mensagens de log
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            # Adiciona o manipulador ao logger
            cls._instance.logger.addHandler(handler)

        return cls._instance  # Retorna a instância única

    def log(self, message):
        """Método para registrar uma mensagem."""
        self.logger.debug(message)  # Registra a mensagem como DEBUG


# Exemplo de uso do Logger Singleton
if __name__ == "__main__":
    logger1 = Logger()
    logger1.log("Esta é a primeira mensagem de log.")

    logger2 = Logger()
    logger2.log("Esta é a segunda mensagem de log.")

    # Verificando se ambas as variáveis apontam para a mesma instância
    print(logger1 is logger2)  # Saída: True
