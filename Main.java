
 int num = Number(prompt("Digita aí: ")) ;
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
 public void move ( int distanceInMeters , string  name  ) { 
 System.out.println ( name + " moved " + distanceInMeters + "m." ) ;
  }
 public void calc ( int num1 , int  num2  ) { 
 int soma = num1 + num2 ;
 int sub = num1 - num2 ;
 int mult = num1 * num2 ;
 int div = num1 / num2 ;
 System.out.println ( "Soma="+soma+" Sub="+sub+" Mult="+mult+" Div=" + div ) ;
  }
 move ( 2 , "2" ) ;
 calc ( num1 , num2 ) ;
 // declaração, implementação e chamada de funções; // ○ if-then-elses e for/while; // ○ entradas e saídas pelo terminal; // ○ instruções de atribuição; // ○ expressões numéricas e booleanas;