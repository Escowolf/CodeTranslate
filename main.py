f = open ("text_file.txt")
strif = f.read()

text = strif.replace("console.log","System.out.println")

text2 = text.replace(": boolean","boolean")
text3 = text2.replace(": number","int")
text4 = text3.replace(": string","string")
text5 = text4.replace(": void","void")

list_of_tokens = text5.split();

text = ""
arrayText = []
arrayText2 = []

for x in list_of_tokens:
  text = text + " " + x
  if x == "{" or x == "}" or x == ";":
    text = text + "\n"
    arrayText.append(text)


# arrayText2.append(arrayText[len(arrayText)-1])

import re

# código TypeScript a ser transpilado
typescript_code = text

# converte variáveis TypeScript em Java
java_code = re.sub(r'var (\w+)\s*\s*(\w+)\s*=\s*(.*);', r'\2 \1 = \3;', typescript_code)

# converte métodos TypeScript em Java
java_code = re.sub(r'function (\w+)\s*\(\s*([^)]*)\s*\)\s*\s*(\w+)\s*\{([^}]*)\}', r'public \3 \1 ( \2 ) { \4 }', java_code)

# java_code = re.sub(r'(\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*\)\s*', r'\2 \1 , \4  \3 , \6 \5', java_code)

java_code = re.sub(r'\( \s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)', r'( \2 \1 , \4  \3', java_code)

# imprime o código Java gerado
print(java_code)

arrayText2 = java_code.split('\n')

path = "Main.java"
write_on_file = lambda f, arrayText2 : [f.write("\n" + nline) for nline in arrayText2]
write_on_file (open (path, "w"), arrayText2)