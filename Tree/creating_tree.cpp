#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:

    int value;
    Node *left;
    Node *right;

    Node(int value)
    {
        this->value=value;
        this->left=NULL;
        this->right=NULL;
    }
};

void preorder(Node *root)
{   
    if(root==NULL)
    {
        return ;
    }
    cout<<root->value<<" ";
    preorder(root->left);
    preorder(root->right);

}
void inorder(Node *root)
{
    if(root==NULL)
    {
        return ;
    }
    inorder(root->left);
    cout<<root->value<<" ";
    inorder(root->right);
}

void postorder(Node *root)
{
    if(root==NULL)
    {
        return ;
    }
    postorder(root->left);
    postorder(root->right);
    cout<<root->value<<" ";
}
int main()
{

    /*
     
      10
     /  \
   20    30
         /
       38
    
    */
    Node *root=new Node(10);
    Node *a=new Node(20);
    Node *b=new Node(30);
    Node *c=new Node(38);

    root->left=a;
    root->right=b;
    b->left=c;

    cout<<"Preorder Traversal: ";

    preorder(root);

    cout<<endl<<"Inorder Traversal: ";

    inorder(root);
    
    return 0;
}