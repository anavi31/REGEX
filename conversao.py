import os

def conversor(caminho):
    print("caminho recebido:", caminho)

    for root, dirs, files in os.walk(caminho):
        print("arquivos encontrados:", files)

        for file in files:
            if file.lower().endswith(".c"):
                print(file, "é um arquivo .c")

                caminho_c = os.path.join(root, file)
                nome_sem_ext = os.path.splitext(file)[0]
                caminho_txt = os.path.join(root, nome_sem_ext + ".txt")

                with open(caminho_c, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                with open(caminho_txt, "w", encoding="utf-8") as f:
                    f.write(conteudo)

                print("convertido de", caminho_c, "para", caminho_txt)
