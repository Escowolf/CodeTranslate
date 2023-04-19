f = open ("text_file.txt")
strif = f.read()

text = strif.replace("console.log","System.out.println")

text2 = text.replace(": boolean","boolean")
text3 = text2.replace(": number","int")
text4 = text3.replace(": string","string")
text5 = text4.replace(": void","void")


list_of_tokens = text5.split();

aspa1 = list_of_tokens.index("(")
aspa2 = list_of_tokens.index(")")

#print(aspa1)
#print(aspa2)

param1 = list_of_tokens[aspa1:aspa2+1]

param = list_of_tokens[aspa1:aspa2+1]
#param1.remove(",")

#print(param1)

for index, x in enumerate(param1):
  if x == "(" or x == ",":
    #print(x)
    par1 = param[index+1];
    param[index+1] = param[index+2]
    param[index+2] = par1
    
#print(param)
#print(text)

#print(text5)

for index, x in enumerate(param):
  list_of_tokens[aspa1+index] = x;

#print(list_of_tokens_text4)

text = ""

for x in list_of_tokens:
  text = text + " " + x
  if x == "{" or x == "}" or x == ";":
    text = text + "\n"


import re

# código TypeScript a ser transpilado
typescript_code = text

# converte variáveis TypeScript em Java
java_code = re.sub(r'var (\w+)\s*:\s*(\w+)\s*=\s*(.*);', r'\2 \1 = \3;', typescript_code)

# converte métodos TypeScript em Java
java_code = re.sub(r'public (\w+)\s*\(\s*([^)]*)\s*\)\s*\s*(\w+)\s*\{([^}]*)\}', r'public \3 \1(\2) {\4}', java_code)

# converte chamadas de console.log em Java
java_code = re.sub(r'console.log\s*\(\s*"([^"]*)"\s*\);', r'System.out.println("\1");', java_code)

# converte operador lógico || em Java
java_code = re.sub(r'\|\|', r'||', java_code)

# converte a chamada do método move em Java
java_code = re.sub(r'move\s*\(\s*(\d+)\s*,\s*(\d+)\s*\);', r'move(\1, "\2");', java_code)

# adiciona tipos genéricos às chamadas do console.log em Java 8
java_code = re.sub(r'System.out.println\("(.*)"\);', r'System.out.println((Object) "\1");', java_code)

# imprime o código Java gerado
print(java_code)