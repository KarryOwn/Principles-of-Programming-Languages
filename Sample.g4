grammar Sample;

program: statement+;

statement: selectStmt
         | updateStmt
         | 'read' 'from' STRING 'as' ID ';'
         | 'display' ID ';';

selectStmt: 'SELECT' columns 'FROM' ID 'WHERE' condition ';';
updateStmt: 'UPDATE' ID 'SET' assignment 'WHERE' condition ';';

columns: ID (',' ID)*;
assignment: ID '=' value;
condition: ID comparator value;
value: STRING | INTEGER;
comparator: '=' | '>' | '<' | '>=' | '<=';

STRING: '"' .*? '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
INTEGER: [0-9]+;
WS: [ \t\r\n]+ -> skip;