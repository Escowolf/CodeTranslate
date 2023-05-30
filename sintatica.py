from lexica import tokenrizar

def valida_codigo(codigo):

  tokens = tokenrizar(codigo)
 
  pos = 0

  # análise sintática
  class SyntaxError(Exception):
    pass

  def consumir(token_tipo):
    nonlocal pos
    if 'TESTEPARAMETROS' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        if pos < len(tokens) and (tokens[pos][0] in [
            'VIRGULA', 'VARIAVEL', 'DOISPONTOS', 'TIPO', 'ESPACO'
        ]):
          pos += 1
        else:
          raise SyntaxError(f"Erro de sintaxe. Esperado '{token_tipo}'.")

    elif 'VERIFICAFUNCTION' in token_tipo:
      while tokens[pos][0] != 'D_CHAVE':
        if pos < len(tokens) and tokens[pos][0] == 'VARIAVEIS':
          parse_variavel()
        elif pos < len(tokens) and tokens[pos][0] == 'BREAK':
          parse_break()
        elif pos < len(tokens) and tokens[pos][0] == 'RETURN':
          parse_return()
        elif pos < len(tokens) and tokens[pos][0] == 'CONSOLE':
          parse_console()
        elif pos < len(tokens) and tokens[pos][0] == 'IF':
          parse_if()
        elif pos < len(tokens) and tokens[pos][0] == 'FOR':
          parse_for()
        elif pos < len(tokens) and tokens[pos][0] == 'WHILE':
          parse_while()
        elif pos < len(tokens) and tokens[pos][0] == 'ELSE':
          parse_else()
        else:
          pos += 1
    elif 'PARAMETROCONSOLE' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        # print(f'---------{tokens[pos][0]}')
        if pos < len(tokens) and tokens[pos][0] in [
            'STRING', 'VARIAVEL', 'ESPACO'
        ]:
          pos += 1
        else:
          pos += 1
    elif 'PARAMETROWHILE' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        # print(tokens[pos][0])
        pos += 1
    elif 'PARAMETROFOR' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        pos += 1
    elif 'PARAMETROIF' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        pos += 1
    elif 'PARAMETRORETURN' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        pos += 1
    elif 'VERIFICAVALOR' in token_tipo:
      while tokens[pos][0] != 'PONTOVIRGULA':
        if pos < len(tokens) and (tokens[pos][0] in [
            'VARIAVEL', 'NUMBER', 'STRING', 'BOOLEAN', 'SOMA', 'SUBTRACAO',
            'MULTIPLICACAO', 'DIVISAO', 'ESPACO'
        ]):
          pos += 1
        elif pos < len(tokens) and tokens[pos][0] == 'PARSENUMBER':
          parse_number()
        elif pos < len(tokens) and tokens[pos][0] == 'PROMPT':
          parse_prompt()
        else:
          raise SyntaxError(f"----Erro de sintaxe. Esperado '{token_tipo}'.")
    elif 'DADOSFUNCTION' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        if pos < len(tokens) and (tokens[pos][0] in [
            'VARIAVEL', 'NUMBER', 'STRING', 'BOOLEAN', 'SOMA', 'SUBTRACAO',
            'MULTIPLICACAO', 'DIVISAO', 'ESPACO', 'VIRGULA'
        ]):
          pos += 1

    elif 'PARAMETRONUMBER' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        if pos < len(tokens) and (tokens[pos][0] in ['PROMPT']):
          parse_prompt()
        elif pos < len(tokens) and (tokens[pos][0] in [
            'VARIAVEL', 'NUMBER', 'SOMA', 'SUBTRACAO', 'MULTIPLICACAO',
            'DIVISAO', 'ESPACO'
        ]):
          pos += 1
        else:
          raise SyntaxError(f"----Erro de sintaxe. Esperado '{token_tipo}'.")
    elif 'PARAMETROPROMPT' in token_tipo:
      while tokens[pos][0] != 'D_PAREN':
        if pos < len(tokens) and (tokens[pos][0] in ['ESPACO']):
          pos += 1
        else:
          raise SyntaxError("----Erro de sintaxe. Apenas STRING no prompt().")
    elif pos < len(tokens) and (tokens[pos][0] in token_tipo):
      # print(tokens[pos][0])
      # print(f'-------{tokens[pos][0]}')
      pos += 1
    else:
      raise SyntaxError(f"Erro de sintaxe. Esperado '{token_tipo}'.")

  def parse_variavel():
    consumir(['VARIAVEIS'])
    consumir(['VARIAVEL'])
    consumir(['ESPACO'])
    consumir(['DOISPONTOS'])
    consumir(['ESPACO'])
    # Analisar o tipo
    consumir(['TIPO'])
    consumir(['ESPACO'])
    consumir(['IGUAL'])
    consumir(['ESPACO'])
    consumir(['VERIFICAVALOR'])

    # Analisar a expressão
    consumir(['PONTOVIRGULA'])
    consumir(['ESPACO'])

  def parse_funcao():
    consumir(['FUNCTION'])
    consumir(['VARIAVEL'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])

    # Analisar os parâmetros
    consumir(['TESTEPARAMETROS'])

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

  def parse_if():
    consumir(['IF'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])
    consumir(['PARAMETROIF'])
    consumir(['D_PAREN'])
    consumir(['ESPACO'])
    consumir(['E_CHAVE'])
    consumir(['ESPACO'])
    # Analisar o corpo da função
    consumir(['VERIFICAFUNCTION'])
    consumir(['D_CHAVE'])
    consumir(['ESPACO'])

  def parse_for():
    consumir(['FOR'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])
    consumir(['PARAMETROFOR'])
    consumir(['D_PAREN'])
    consumir(['ESPACO'])
    consumir(['E_CHAVE'])
    consumir(['ESPACO'])
    # Analisar o corpo da função
    consumir(['VERIFICAFUNCTION'])
    consumir(['D_CHAVE'])
    consumir(['ESPACO'])

  def parse_while():
    consumir(['WHILE'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])
    consumir(['PARAMETROWHILE'])
    consumir(['D_PAREN'])
    consumir(['ESPACO'])
    consumir(['E_CHAVE'])
    consumir(['ESPACO'])
    # Analisar o corpo da função
    consumir(['VERIFICAFUNCTION'])
    consumir(['D_CHAVE'])
    consumir(['ESPACO'])

  def parse_console():
    consumir(['CONSOLE'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])
    consumir(['PARAMETROCONSOLE'])
    consumir(['D_PAREN'])
    consumir(['ESPACO'])
    consumir(['PONTOVIRGULA'])
    consumir(['ESPACO'])

  def parse_break():
    consumir(['BREAK'])
    consumir(['ESPACO'])
    consumir(['PONTOVIRGULA'])
    consumir(['ESPACO'])

  def parse_return():
    consumir(['RETURN'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])

    #verificar retorno
    consumir(['PARAMETRORETURN'])

    consumir(['D_PAREN'])
    consumir(['ESPACO'])
    consumir(['PONTOVIRGULA'])
    consumir(['ESPACO'])

  def parse_else():
    consumir(['ELSE'])
    consumir(['ESPACO'])
    if (tokens[pos][0] != 'IF'):

      consumir(['E_CHAVE'])
      consumir(['ESPACO'])
      consumir(['VERIFICAFUNCTION'])
      consumir(['D_CHAVE'])
      consumir(['ESPACO'])

    else:
      parse_if()

  def parse_chamadafunction():
    consumir(['VARIAVEL'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])
    consumir(['DADOSFUNCTION'])
    consumir(['D_PAREN'])
    consumir(['ESPACO'])
    consumir(['PONTOVIRGULA'])
    consumir(['ESPACO'])

  def parse_number():
    consumir(['PARSENUMBER'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])
    consumir(['PARAMETRONUMBER'])
    consumir(['D_PAREN'])
    consumir(['ESPACO'])

  def parse_prompt():
    consumir(['PROMPT'])
    consumir(['ESPACO'])
    consumir(['E_PAREN'])
    consumir(['ESPACO'])
    consumir(['PARAMETROPROMPT'])
    consumir(['D_PAREN'])
    consumir(['ESPACO'])

  # Função principal para a análise sintática
  def parse_program():
    while pos < len(tokens) - 1:
      if tokens[pos][0] == 'VARIAVEIS':
        parse_variavel()
      elif tokens[pos][0] == 'FUNCTION':
        parse_funcao()
      elif tokens[pos][0] == 'IF':
        parse_if()
      elif tokens[pos][0] == 'FOR':
        parse_for()
      elif tokens[pos][0] == 'WHILE':
        parse_while()
      elif tokens[pos][0] == 'CONSOLE':
        parse_console()
      elif tokens[pos][0] == 'ELSE':
        parse_else()
      elif tokens[pos][0] == 'PARSENUMBER':
        parse_number()
      elif tokens[pos][0] == 'PROMPT':
        parse_prompt()
      elif tokens[pos][0] == 'VARIAVEL':
        parse_chamadafunction()
      else:
        raise SyntaxError(f"Token inesperado: {tokens[pos][0]}")

  parse_program()
