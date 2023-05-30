substituir = {
  "console.log": "System.out.println",
  ": boolean ": "boolean ",
  ": number ": "int ",
  ": string ": "String ",
  ": void ": "void "
}
def substituicao(codigo):
  for chave, valor in substituir.items():
    codigo = codigo.replace(chave, valor)
  return codigo