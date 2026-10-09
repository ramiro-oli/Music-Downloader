from yt_dlp import YoutubeDL

# Função que pede as urls e organiza elas em uma lista
def organizar_urls():
    # Lista que vai receber as urls
    urls = []

    # Loop para receber quantas urls o usuário desejar
    while True:
        # Pede uma url ao usuário e insere na lista
        url = input("Insira a url do vídeo: ")
        urls.append(url)

        # Verifica se o usuário vai adicionar mais urls ou deseja parar
        escolha = int(input("Deseja inserir mais urls? (1 para sim/0 para não): "))
        match escolha:
            case 0:
                break
            case 1:
                continue
            case _:
                print("Ação inválida")

    # Devolve a lista com as urls
    return urls

# Função que baixa os vídeos
def baixar_videos(urls):
    # Dicionário que determina configurações do arquivo
    config = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    # Percorre cada url que o usuário mandou
    for url in urls:
        # Tenta baixar
        try:
            with YoutubeDL(config) as ydl:
                ydl.download([url])
        # Caso não consiga baixar
        except Exception:
            print("Erro ao baixar")

# Roda o programa
urls = organizar_urls()
baixar_videos(urls)