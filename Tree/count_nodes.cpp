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
Node *input()
{
    int val;
    cin>>val;

    Node *root=new Node(val);
    queue<Node *>q;

    q.push(root);
    while(!q.empty())
    {
        Node *f=q.front();
        q.pop();

        int l,r;
        cin>>l>>r;
        
        Node *myleft,*myright;

        if(l==-1)
        {
            myleft=NULL;
        }
        else
        {
            myleft=new Node(l);
        }
        if(r==-1)
        {
            myright=NULL;
        }
        else
        {
            myright=new Node(r);
        }

        f->left=myleft;
        f->right=myright;

        if(f->left)
        {
            q.push(f->left);
        }
        if(f->right)
        {
            q.push(f->right);
        }


        
    }

    return root;

    
}

int count_nodes(Node *root)
{
    if(root==NULL)
    {
        return 0;
    }
    int l=count_nodes(root->left);
    int r=count_nodes(root->right);

    return l+r+1;
}
int main()
{
    Node *root=input();

    cout<<"Total Nodes: "<<count_nodes(root)<<endl;

    return 0;

}