f = open ("text_file.txt")

strif = f.read()

text = strif.replace("console.log","System.out.println")

text2 = text.replace(": boolean","boolean")

text3 = text2.replace(": number","int")

text4 = text3.replace(": string","String")

text5 = text4.replace(": void","void")

list_of_tokens = text5.split();

text = """
public class Main {
  
"""

for x in list_of_tokens:
  text = text + " " + x
  if x == "{" or x == "}" or x == ";":
    text = text + "\n"

text = text + """

  }
}
"""

import re

typescript_code = text

java_code = re.sub(r'var (\w+)\s*\s*(\w+)\s*=\s*(.*);', r'\2 \1 = \3;', typescript_code)

if re.search(r'=\s* Number \( prompt \( " Digita aí : " \) \) \s*;', java_code):
  java_code = re.sub(r'=\s* Number \( prompt \( " Digita aí : " \) \) \s*;', r'= Integer.parseInt(System.console().readLine());', java_code)

if re.search(r'=\s* prompt \( " Digita aí : " \) \s*;', java_code):
  java_code = re.sub(r'=\s* prompt \( " Digita aí : " \) \s*;', r'= System.console().readLine();', java_code)

java_code = re.sub(r'function (\w+)\s*\(\s*([^)]*)\s*\)\s*\s*(\w+)\s*\{([^}]*)\}', r'public static \3 \1 ( \2 ) { \4 }', java_code)

if re.search(r'\(\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*\)\s*', java_code):
 java_code = re.sub(r'(\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)\s*\)\s*', r'\2 \1 , \4  \3 , \6 \5', java_code)

java_code = re.sub(r'\( \s*(\w+)\s+(\w+)\s*,\s*(\w+)\s+(\w+)', r'( \2 \1 , \4  \3', java_code)

print(java_code)

arrayText1 = java_code.split('\n')

text = ""

for x in arrayText1:
  if re.search(r'readLine', x):
    if not re.search(r'public\s+static\s+void\s+main\s*\(\s*String\[\]\s+args\s*\)\s*\{', text):
      text = text + "\n public static void main(String[] args) { \n "  
  text = text + "\n " + x

arrayText = text.split('\n')

path = "Main.java"

write_on_file = lambda f, arrayText : [f.write("\n" + nline) for nline in arrayText]

write_on_file (open (path, "w"), arrayText)
