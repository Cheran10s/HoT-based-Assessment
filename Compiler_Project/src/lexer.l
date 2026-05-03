%{
#include "y.tab.h"
%}

%%
[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[a-zA-Z]+   { return ID; }
"+"         { return PLUS; }
"="         { return ASSIGN; }
";"         { return SEMICOLON; }
[ \t\n]+    ;
%%

int yywrap() { return 1; }
