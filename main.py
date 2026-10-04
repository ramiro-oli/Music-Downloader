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
def baixar_vídeos(urls):
    # Cria um dicionário que salva onde deve ser salvo e o nome do arquivo
    config = {
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    # Baixa os vídeos com base nas configurações
    with YoutubeDL(config) as ydl:
        ydl.download(urls)

# Roda o programa
urls = organizar_urls()
baixar_vídeos(urls)