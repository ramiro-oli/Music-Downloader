from yt_dlp import YoutubeDL

# Função que baixa os vídeos
def baixar_videos(urls):
    with YoutubeDL() as ydl:
        ydl.download(urls)

#Função que organiza as urls digitadas pelo usuário
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

# Roda o programa
urls = organizar_urls()
baixar_videos(urls)