# HoT-based-Assessment
# Compiler Design DSL

## Description
Simple DSL compiler using Flex and Bison with AST support.

## Structure
src/, test/, output/, docs/

## Run
flex lexer.l
bison -d parser.y
gcc lex.yy.c parser.tab.c -o compiler
./compiler < test/input.txt

## Output
Valid Statement


## Student Details
Name: R Cheran
Reg No: RA2311026050276
