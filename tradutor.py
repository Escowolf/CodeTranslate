import re

def transforme_java(codigoType):
  codigo_java = """
  public class Main {
    
  """
  
  for token in codigoType:
    codigo_java += " " + token
    if token == "{" or token == "}" or token == ";":
      codigo_java += "\n"
  
  codigo_java += """
  
    }
  }
  """
  
  codigo_java = re.sub(
    r'function\s*(\w+)\s*\(\s*([^)]*)\s*\)\s*\s*(\w+)\s*\{([^}]*)\}',
    r'public static \3 \1 ( \2 ) { \4 }', 
    codigo_java)

  codigo_java = re.sub(
    r'(var|let|const)\s*(\w+)\s*\s*(\w+)\s*=\s*(.*);', 
    r'\3 \2 = \4;',
    codigo_java)

  codigo_java = re.sub(
    r'\s*(\w+)\s+(int|String|boolean)\s*', 
    r' \2 \1 ', 
    codigo_java)
  
  if re.search(
    r'=\s*Number\s*\((\s*prompt\s*\(\s*\))\s+\)\s+;', 
    codigo_java):
      codigo_java = re.sub(
        r'=\s*Number\s*\(\s*prompt\s*\(\s*\)\s*\)\s*;',
        r'= Integer.parseInt(System.console().readLine());',
        codigo_java)
  
  if re.search(
    r'=\s*prompt\s*\(\s*\)\s*;', 
    codigo_java):
      codigo_java = re.sub(
        r'=\s*prompt\s*\(\s*\)\s*;',
        r'= System.console().readLine();', 
        codigo_java)
  

  
  array_codigo = codigo_java.split('\n')
  
  codigo_java = ""
  
  for x in array_codigo:
    if re.search(r'readLine', x):
      if not re.search(
          r'public\s+static\s+void\s+main\s*\(\s*String\[\]\s+args\s*\)\s*\{',
          codigo_java):
        codigo_java = codigo_java + "\n public static void main(String[] args) { \n "
    codigo_java = codigo_java + "\n " + x


  return codigo_java