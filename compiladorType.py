import re
# análise léxica
# Lista de tokens
tokens = [
    ('TIPO', r'number|string|number|void|boolean'),
    ('VARIAVEIS', r'let|var|const'),
    ('NUMBER', r'\d+'),
    ('STRING', r'"([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\''),
    ('BOOLEAN', r'true|false'),
    ('PONTOVIRGULA', r';'),
    ('DOISPONTOS', r':'),
    ('VIRGULA', r','),
    ('E_PAREN', r'\('),
    ('D_PAREN', r'\)'),
    ('E_CHAVE', r'{'),
    ('D_CHAVE', r'}'),
    ('IGUAL', r'='),
    ('ESPACO', r'\s+'),
    ('SOMA', r'\+'),
    ('SUBTRACAO', r'\-'),
    ('DIVISAO', r'\/'),
    ('MULTIPLICACAO', r'\*'),
    ('FUNCTION', r'function'),
    ('VARIAVEL', r'[a-zA-Z_][a-zA-Z_0-9]*')
]

def tokenrizar(codigo):
    lista_de_tokens = []
    pos = 0

    while pos < len(codigo):
        comp = None

        for token in tokens:
            token_nome, token_padrao = token
            regex = re.compile(token_padrao)
            comp = regex.match(codigo, pos)


            if comp:
                token_valor = comp.group(0)
                lista_de_tokens.append((token_nome, token_valor))
                pos = comp.end(0)
                break

        if not comp:
          print(f"Token inválido: {codigo[pos]}")
          pos += 1

    return lista_de_tokens

# análise sintática
class SyntaxError(Exception):
    pass

def parse(tokens):
    pos = 0

    def consumir(token_tipo):
        nonlocal pos
        if 'testeParametros' in token_tipo:
            while tokens[pos][0] != 'D_PAREN':
             
              if pos < len(tokens) and (tokens[pos][0] in ['VIRGULA','VARIAVEL', 'DOISPONTOS', 'TIPO', 'ESPACO']):
                  pos += 1
              else:
                  raise SyntaxError(f"Erro de sintaxe. Esperado '{token_tipo}'.")

        elif 'VERIFICAFUNCTION' in token_tipo:
            while tokens[pos][0] != 'D_CHAVE':
              # TODO loop infinito
              if tokens[pos][0] == 'VARIAVEIS':
                parse_variavel()
                pos += 1
        elif pos < len(tokens) and (tokens[pos][0] in token_tipo):
           
            pos += 1
        else:
            raise SyntaxError(f"Erro de sintaxe. Esperado '{token_tipo}'.")

    def parse_variavel():
        consumir(['VARIAVEIS'])
        consumir(['ESPACO'])
        consumir(['VARIAVEL'])
        consumir(['ESPACO'])
        consumir(['DOISPONTOS'])
        consumir(['ESPACO'])
        # Analisar o tipo
        consumir(['TIPO'])
        consumir(['ESPACO'])
        consumir(['IGUAL'])
        consumir(['ESPACO'])
        consumir(['VARIAVEL', 'NUMBER', 'STRING', 'BOOLEAN'])
        consumir(['ESPACO'])
        # Analisar a expressão
        consumir(['PONTOVIRGULA'])

        consumir(['ESPACO'])


    def parse_funcao():
        consumir(['FUNCTION'])
        consumir(['ESPACO'])
        consumir(['VARIAVEL'])
        consumir(['ESPACO'])
        consumir(['E_PAREN'])
        consumir(['ESPACO'])
      
        # Analisar os parâmetros
        consumir(['testeParametros'])
      
        consumir(['D_PAREN'])
        consumir(['ESPACO'])
        consumir(['DOISPONTOS'])
        consumir(['ESPACO'])
        consumir(['TIPO'])
        consumir(['ESPACO'])
        consumir(['E_CHAVE'])
        consumir(['ESPACO'])
        # Analisar o corpo da função
        consumir(['VERIFICAFUNCTION'])
      
        consumir(['D_CHAVE'])
        consumir(['ESPACO'])


    # Função principal para a análise sintática
    def parse_program():
        while pos < len(tokens)-1:
            if tokens[pos][0] == 'VARIAVEIS':
                parse_variavel()
            elif tokens[pos][0] == 'FUNCTION':
                parse_funcao()
            else:
                raise SyntaxError(f"Token inesperado: {tokens[pos][0]}")
              
    parse_program()

# # análise semântica

# class SemanticError(Exception):
#     pass

# def analyze_semantics(tokens):
#     tabela_tipos = {}

#     def analisar_variavel():
#         variavel_nome = tokens[pos + 1][1]
#         variavel_tipo = None

#         if variavel_nome in tabela_tipos:
#             raise SemanticError(f"Erro semântico: Variável '{variavel_nome}' já declarada.")

#         if tokens[pos + 3][0] == 'VARIAVEL':
#             variavel_tipo = tokens[pos + 3][1]
#         else:
#             raise SemanticError("Erro semântico: Tipo de variável inválido.")

#         tabela_tipos[variavel_nome] = variavel_tipo

#     def analisar_funcao():
#         funcao_nome = tokens[pos + 1][1]
#         parametro_tipo = []
#         return_tipo = None

#         if funcao_nome in tabela_tipos:
#             raise SemanticError(f"Erro semântico: Função '{funcao_nome}' já declarada.")

#         pos += 3  # Avança para o token de parâmetros

#         while tokens[pos][0] != 'D_PAREN':
#             if tokens[pos][0] == 'VARIAVEL':
#                 parametro_tipo.append(tokens[pos][1])
#             pos += 1

#         pos += 2  # Avança para o token de tipo de retorno

#         if tokens[pos][0] == 'VARIAVEL':
#             return_tipo = tokens[pos][1]
#         else:
#             raise SemanticError("Erro semântico: Tipo de retorno inválido.")

#         tabela_tipos[funcao_nome] = {'parameters': parametro_tipo, 'return_tipo': return_tipo}

#     def analyze_program():
#         pos = 0

#         while pos < len(tokens):
#             if tokens[pos][0] == 'LET':
#                analisar_variavel()
#             elif tokens[pos][0] == 'FUNCTION':
#                 analisar_funcao()
#             else:
#                 raise SemanticError(f"Token inesperado: {tokens[pos][0]}")

#             pos += 1

#     analyze_program()

# Exemplo de uso
codigo = '''let x : number = 5 ;
let y : string = "Hello" ; 
function add ( a : number , b : number ) : number {
    var x : boolean = true ;
    
} '''

tokens = tokenrizar(codigo)
parse(tokens)
# analyze_semantics(tokens)
