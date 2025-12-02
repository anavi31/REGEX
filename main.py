import re

TOKEN_TYPES = [
    ("Numero",   r'\d+(\.\d+)?'),
    ("ID",       r'[A-Za-z_][A-Za-z0-9_]*'),
    ("Operador", r'[\+\-\*/=]'),
    ("Parentesis_de_Abertura", r'\('),
    ("Parentesis_de_Fechamento", r'\)'),
    ("Espaco",   r'[ \t\n]+'),
]


master_pattern = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES)
)


def lexer(code):
    tokens = []
    symbol_table = {}     # nome → id_num
    next_symbol_id = 1    # contador de IDs numéricos

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
    codigo = open('program.c').read()
    tokens, symbol_table = lexer(codigo.read())

    print("Tokens:")
    for t in tokens:
        print(t)

    print("\nTabela de Símbolos:")
    for name, idnum in symbol_table.items():
        print(f"{idnum} → {name}")


if __name__ == "__main__":
    main()