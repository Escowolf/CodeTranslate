

 
 public class Main {
   
  public static void move ( int distanceInMeters , String  name  ) { 
  System.out.println ( name + " moved " + distanceInMeters + "m." ) ;
   }
  public static void calc ( int num1 , int  num2  ) { 
  int soma = num1 + num2 ;
  int sub = num1 - num2 ;
  int mult = num1 * num2 ;
  int div = num1 / num2 ;
  System.out.println ( "Soma="+soma+" Sub="+sub+" Mult="+mult+" Div=" + div ) ;
   }
 public static void main(String[] args) { 
 
  int num = Integer.parseInt(System.console().readLine());
  String strin = System.console().readLine();
  int num1 = 2 ;
  int num2 = 2 ;
  while ( num != 8 ) {
  System.out.println ( num ) ;
  if ( num < 1 || num > 10 ) {
  System.out.println ( "That is not between 1 and 10" ) ;
  break ;
  }
  else {
  num++ ;
  }
  }
  move ( 2 , "2" ) ;
  calc ( num1 , num2 ) ;
  // declaração, implementação e chamada de funções; // ○ if-then-elses e for/while; // ○ entradas e saídas pelo terminal; // ○ instruções de atribuição; // ○ expressões numéricas e booleanas;
 
   }
 }
 