#include <stdio.h>
#include <stdlib.h>
#include "ast.h"

Node* createNode(char *type, int value) {
    Node *n = (Node*)malloc(sizeof(Node));
    n->type = type;
    n->value = value;
    n->left = n->right = NULL;
    return n;
}

void printAST(Node *root) {
    if (!root) return;
    printf("%s ", root->type);
    printAST(root->left);
    printAST(root->right);
}
