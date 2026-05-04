#include<bits/stdc++.h>
using namespace std;
class Node
{
  public:
  int val;
  Node *left;
  Node *right;

  Node(int val)
  {

    this->val=val;
    this->left=NULL;
    this->right=NULL;

  }

};
Node *input()
{
    int value;
    cin>>value;

    Node *root=new Node(value);

    queue<Node*>q;
    q.push(root);

    while(!q.empty())
    {
        Node *f=q.front();
        q.pop();
        int l,r;
        cin>>l>>r;

        Node *myleft,*myright;
        if(l== -1)
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
bool nodehas(Node *root,int x)
{
    if(root==NULL)
    {
        return false;
    }
    if(root->val==x)
    {
        return true;
    }
    bool l= nodehas(root->left,x);
    bool r=nodehas(root->right,x);

    if(l==true || r== true)
    {
        return true;

    }
    else
    {
        return false;
    }

}
int main()
{

    Node *root=input();

    int x;
    cin>>x;
    if(nodehas(root,x))
    {
        cout<<"Node is Present"<<endl;
    }
    else
    {
        cout<<"Not present"<<endl;
    }

}