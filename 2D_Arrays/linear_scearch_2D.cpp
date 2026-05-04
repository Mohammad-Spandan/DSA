#include<bits/stdc++.h>
using namespace std;
int main()
{
    int row,col;
    cin>>row>>col;

    int arr [row] [col];

    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            cin>>arr[i][j];
        }
    }

    int target;
    cin>> target;
    bool has=0;
    pair<int,int>p;

    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            if(arr[i][j]==target)
            {
               has=1;
               p.first=i;
               p.second=j;
            }
        }
    }

    if(has==1)
    {
        cout<<"YES"<<endl;
        cout<<"The pair index : ("<<p.first<<" ,"<<p.second<<")";
    }
    else
    {
        cout<<"NO"<<endl;
    }

    return 0;

}