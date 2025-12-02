import re
import os
import sys

TOKEN_TYPES = [
    ("Numero",   r'\d+(\.\d+)?'),
    ("ID",       r'[A-Za-z_][A-Za-z0-9_]*'),
    ("Operador", r'==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|%='
                 r'|&&|\|\||<<|>>|[+\-*/=%<>!&|^~]'),
    ("Parentesis_de_Abertura", r'\('),
    ("Parentesis_de_Fechamento", r'\)'),
    ("Chave_Abertura", r'\{'),
    ("Chave_Fechamento", r'\}'),
    ("Ponto_e_Virgula", r';'),
    ("Virgula", r','),
    ("Espaco",   r'[ \t\n\r]+'),
    ("String",   r'"([^"\\]|\\.)*"'),
    ("Char",     r"'([^'\\]|\\.)'"),
]

master_pattern = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES)
)

def conversor(pasta=None):
    if pasta is None:
        try:
            pasta = os.path.dirname(os.path.abspath(__file__)) or os.getcwd()
        except NameError:
            pasta = os.getcwd()

    for entry in os.listdir(pasta):
        if entry.lower().endswith(".c"):
            caminho_c = os.path.join(pasta, entry)
            nome_sem_ext = os.path.splitext(entry)[0]
            caminho_txt = os.path.join(pasta, nome_sem_ext + ".txt")

            with open(caminho_c, "r", encoding="utf-8", errors="ignore") as f_in:
                conteudo = f_in.read()

            with open(caminho_txt, "w", encoding="utf-8") as f_out:
                f_out.write(conteudo)

            return caminho_txt
    return None

def lexer(code):
    tokens = []
    symbol_table = {}
    next_symbol_id = 1

    for match in master_pattern.finditer(code):
        token_type = match.lastgroup
        value = match.group()

        if token_type == "Espaco":
            continue

        if token_type == "ID":
            if value not in symbol_table:
                symbol_table[value] = next_symbol_id
                next_symbol_id += 1
            tokens.append((token_type, symbol_table[value]))
        else:
            tokens.append((token_type, value))

    return tokens, symbol_table

def main():
    txt_path = conversor() 

    if txt_path is None:
        print("Abortando: coloque um arquivo .c na mesma pasta deste script e rode novamente.")
        sys.exit(1)

    with open(txt_path, "r", encoding="utf-8") as f:
        codigo = f.read()

    tokens, symbol_table = lexer(codigo)

    print("\nTokens:")
    for t in tokens:
        print(t)

    print("\nTabela de Símbolos:")
    items = sorted(symbol_table.items(), key=lambda x: x[1])
    for name, idnum in items:
        print(f"{idnum} → {name}")

if __name__ == "__main__":
    main()