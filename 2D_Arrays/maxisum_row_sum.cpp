#include<bits/stdc++.h>
using namespace std;
int main()
{
    int row,col;
    cin>>row>>col;

    int arr[row][col];

    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            cin>>arr[i][j];
        }
    }

    
    
    int maxsum=INT_MIN;

    for(int i=0;i<row;i++)
    {
        int rowsum=0;

        for(int j=0;j<col;j++)
        {
            rowsum=rowsum+arr[i][j];
        }
        maxsum=max(maxsum,rowsum);
        
    }
    cout<<maxsum<<endl;
}