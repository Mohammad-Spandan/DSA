#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int e=0;
    int o=0;
int pos=0;
    int neg=0;
    while(n--)
    {
        int x;
        cin>>x;
        if(x%2==0)
        {
            e++;
        }
        if (x%2 !=0)
        {
            o++;
        }
        if(x>0)
        {
            pos++;
        }
        if(x<0)
        {
            neg++;
        }

        
    }
    cout<<"Even: "<<e<<endl;
    cout<<"Odd: "<<o<<endl;
    cout<<"Positive: "<<pos<<endl;
    cout<<"Negative: "<<neg<<endl;

 }