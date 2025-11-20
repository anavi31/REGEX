import os

def conversor(pasta):

    for root, dirs, files in os.walk(pasta):
        for file in files:
            if file.lower().endswith(".c"):
                caminho_c = os.path.join(root, file)
                caminho_txt = os.path.join(root, file[:-2] + ".txt")

                with open(caminho_c, "r", encoding="utf-8") as arquivo_c:
                    conteudo = arquivo_c.read()

                with open(caminho_txt, "w", encoding="utf-8") as arquivo_txt:
                    arquivo_txt.write(conteudo)

                print(f"Convertido: {caminho_c} para {caminho_txt}")