#include<bits/stdc++.h>
using namespace std;
void fact(int n)
{
        int fact=1;
    if(n==0)
    {
        cout<<1<<endl;
        
    }
    else
    { 

    for(int i=n;i>=1;i--)
    {
        fact=fact*i;
    }
    cout<<fact<<endl;

    }
 
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;

        fact(n);
    }
}