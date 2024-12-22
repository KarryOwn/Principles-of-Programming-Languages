grammar Sample;

program: expression;

expression: expression (Add | Sub) term | term;

term: term (Mul | Div) factor | factor;

factor: funcCall | '(' expression ')'| Integer;

funcCall: Id '(' (expression (',' expression)*)? ')';  // Function calls

Add: '+';
Sub: '-';
Mul: '*';
Div: '/';

Id: [a-zA-Z_][a-zA-Z_0-9]*;  
Integer: [0-9]+;            

WS: [ \t\r\n]+ -> skip;     