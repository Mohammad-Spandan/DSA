#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int temp=n;
    int rev=0;
    while(temp>0)
    {
        int r=temp%10;
        rev=rev*10+r;
        temp=temp/10;
    }
    cout<<rev<<endl;
    if(rev==n)
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;

    }
    
}