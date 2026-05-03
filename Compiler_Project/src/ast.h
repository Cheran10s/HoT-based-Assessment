#ifndef AST_H
#define AST_H

typedef struct Node {
    char *type;
    int value;
    struct Node *left, *right;
} Node;

Node* createNode(char *type, int value);
void printAST(Node *root);

#endif
