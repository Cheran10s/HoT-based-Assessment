#include <stdio.h>

int main() {
    printf("Run using: flex lexer.l && bison -d parser.y && gcc lex.yy.c parser.tab.c -o compiler\n");
    return 0;
}
