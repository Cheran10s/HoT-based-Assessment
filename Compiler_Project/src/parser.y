%{
#include <stdio.h>
#include "ast.h"
%}

%token NUMBER ID PLUS ASSIGN SEMICOLON

%%

stmt: ID ASSIGN expr SEMICOLON { printf("Valid Statement\n"); };

expr: expr PLUS NUMBER
    | NUMBER
    ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(char *s) {
    printf("Error: %s\n", s);
    return 0;
}
