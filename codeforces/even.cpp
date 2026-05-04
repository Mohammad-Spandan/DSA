#include<bits/stdc++.h>
using namespace std;
void even(int n)
{
  
    for(int i=1;i<=n;i++)
    {
        if(i%2==0)
        {
            cout<<i<<endl;
        }
    }


    
   
}
int main()
{
    int n;
    cin>>n;
    if(n==1)
    {
        cout<<-1<<endl;
        return 0;
    }
    even(n);

}