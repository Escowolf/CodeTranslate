import re
f = open("text_file.txt")

string_f = f.read()

toReplace = {
  "console.log": "System.out.println",
  ": boolean": "boolean",
  ": number": "int",
  ": string": "String",
  ": void": "void"
}

for key, value in toReplace.items():
  string_f = string_f.replace(key, value)

list_of_tokens = string_f.split()

text = """
public class Main {
  
"""

for x in list_of_tokens:
  text += " " + x
  if x == "{" or x == "}" or x == ";":
    text += "\n"

text += """

  }
}
"""

java_code = re.sub(r'var (\w+)\s*\s*(\w+)\s*=\s*(.*);', r'\2 \1 = \3;', text)

java_code = re.sub(r'function (\w+)\s*\(\s*([^)]*)\s*\)\s*\s*(\w+)\s*\{([^}]*)\}', r'public static \3 \1 ( \2 ) { \4 }', java_code)

java_code = re.sub(r'\( \s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)', r'( \2 \1 , \4  \3', java_code)

if re.search(r'=\s* Number \( prompt \( " Digita aí : " \) \) \s*;', java_code):
  java_code = re.sub(r'=\s* Number \( prompt \( " Digita aí : " \) \) \s*;', r'= Integer.parseInt(System.console().readLine());', java_code)

if re.search(r'=\s* prompt \( " Digita aí : " \) \s*;', java_code): 
  java_code = re.sub(r'=\s* prompt \( " Digita aí : " \) \s*;', r'= System.console().readLine();', java_code)

if re.search(r'\(\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*\)\s*', java_code): 
  java_code = re.sub(r'(\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*\)\s*', r'\2 \1 , \4  \3 , \6 \5', java_code)

array_text = java_code.split('\n')

text = ""

for x in array_text:
  if re.search(r'readLine', x):
    if not re.search(r'public\s+static\s+void\s+main\s*\(\s*String\[\]\s+args\s*\)\s*\{', text):
      text = text + "\n public static void main(String[] args) { \n "
  text = text + "\n " + x

print(text)

array_text = text.split('\n')

path = "Main.java"

write_on_file = lambda f, array_text: [
  f.write("\n" + nline) for nline in array_text
]

write_on_file(open(path, "w"), array_text)
