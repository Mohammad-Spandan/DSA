#include<bits/stdc++.h>
using namespace std;
bool lucky(int n)
{
    string s=to_string(n);
    for(int i=0;i<s.size();i++)
    {
        if(s[i]!='4' && s[i]!='7')
        {
            return false;
        }
    }
    return true;
}
int main()
{
    int a,b;
    cin>>a>>b;
    int cnt=0;
    for(int i=a;i<=b;i++)
    {
        if(lucky(i))
        {
            cout<<i<<endl;
            cnt++;
        }
    }
    if(cnt==0)
    {
        cout<<-1<<endl;
    }
    

}