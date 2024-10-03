# Interface que o cliente espera (por exemplo, um player que só entende MP4)
class MediaPlayer:
    def play(self, filename: str):
        pass

# Classe existente que toca vídeos em formato AVI
class AviPlayer:
    def play_avi(self, filename: str):
        print(f"Playing AVI file: {filename}")

# Adapter que converte AVI para a interface de MP4
class AviToMp4Adapter(MediaPlayer):
    def __init__(self, avi_player: AviPlayer):
        self.avi_player = avi_player

    def play(self, filename: str):
        # Aqui o Adapter converte o comportamento de AVI para o formato esperado (MP4)
        self.avi_player.play_avi(filename)

# Uso
if __name__ == "__main__":
    avi_player = AviPlayer()
    adapter = AviToMp4Adapter(avi_player)

    # O cliente chama o método 'play', mas o Adapter faz a conversão
    adapter.play("video.avi")  # Saída: Playing AVI file: video.avi