dic = [('TIPO', r'number|string|number|void|boolean'), ('ESPACO', r'\s+'),
          ('IF', r'if'),
          ('ELSE', r'else'), ('FOR', r'for'), ('WHILE', r'while'),
          ('CONSOLE', r'console.log'), ('BREAK', r'break'),
          ('RETURN', r'return'), ('PARSENUMBER', r'Number'),
          ('PROMPT', r'prompt'), ('VARIAVEIS', r'let\s+|var\s+|const\s+'),
          ('NUMBER', r'\d+'),
          ('STRING', r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''),
          ('BOOLEAN', r'true|false'), ('PONTOVIRGULA', r';'),
          ('DOISPONTOS', r':'), ('VIRGULA', r','), ('E_PAREN', r'\('),
          ('D_PAREN', r'\)'), ('E_CHAVE', r'{'), ('D_CHAVE', r'}'),
          ('IGUAL', r'='), ('DIFERENTE', r'!='), ('SOMA', r'\+'),
          ('SUBTRACAO', r'\-'), ('DIVISAO', r'\/'), ('OU', r'\|\|'),
          ('E', r'\&\&'), ('MAIORQUE', r'\>'), ('MENORQUE', r'\<'),
          ('MULTIPLICACAO', r'\*'), ('FUNCTION', r'\s*function\s+'),
          ('VARIAVEL', r'[a-zA-Z_][a-zA-Z_0-9]*')]

def verifica_declaracao_uso_variaveis(tokens):
    declaradas = set()
    utilizadas = set()
    tipos = {}

    for token in tokens:
        if token[0] == 'VARIAVEL':
            nome_variavel = token[1]
            if nome_variavel in declaradas:
                raise ValueError(f"Erro semântico. Variável '{nome_variavel}' já foi declarada.")
            utilizadas.add(nome_variavel)
        elif token[0] == 'VARIAVEIS':
            nomes_variaveis = token[1]
            for nome_variavel in nomes_variaveis:
                if nome_variavel in declaradas:
                    raise ValueError(f"Erro semântico. Variável '{nome_variavel}' já foi declarada.")
                declaradas.add(nome_variavel)
        elif token[0] == 'VARIAVEIS':
            nome_variavel = token[1]
            if nome_variavel not in declaradas:
                raise ValueError(f"Erro semântico. Variável '{nome_variavel}' não foi declarada.")
            utilizadas.add(nome_variavel)
       

    for variavel in utilizadas:
        if variavel not in declaradas:
            raise ValueError(f"Erro semântico. Variável '{variavel}' não foi declarada.")

def verifica_tipos(tokens):
    for token in tokens:
        if token[0] == 'TIPO':
            nome_variavel = token[1]
            valor = token[2]
            tipo_variavel = dic.get(nome_variavel)
            if tipo_variavel is None:
                raise ValueError(f"Erro semântico. Tipo da variável '{nome_variavel}' não foi declarado.")
            if not verifica_compatibilidade_tipos(tipo_variavel, valor):
                raise ValueError(f"Erro semântico. Incompatibilidade de tipos na atribuição da variável '{nome_variavel}'.")    

def verifica_compatibilidade_tipos(tipo_variavel, valor):
    if tipo_variavel == 'int' and not isinstance(valor, int):
        return False
    elif tipo_variavel == 'float' and not isinstance(valor, float):
        return False
    elif tipo_variavel == 'str' and not isinstance(valor, str):
        return False
    elif tipo_variavel == 'bool' and not isinstance(valor, bool):
        return False
    # Adicione condições para outros tipos de dados, se necessário
    else:
        return True