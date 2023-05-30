from substituicao import substituicao
from tradutor import transforme_java
from cria_arquivo import cria_arquivo
from sintatica import valida_codigo

arquivo = open("text_file.txt")

type_arquivo = arquivo.read()

valida_codigo(type_arquivo)

type_arquivo = substituicao(type_arquivo)

lista_tokens = type_arquivo.split()

codigo_java = transforme_java(lista_tokens)

print(codigo_java)

array_codigo = codigo_java.split('\n')

cria_arquivo(array_codigo)