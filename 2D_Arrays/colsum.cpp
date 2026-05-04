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
        int colsum=0;

        for(int j=0;j<col;j++)
        {
            colsum=colsum+arr[j][i];
        }
        maxsum=max(maxsum,colsum);
        
    }
    cout<<maxsum<<endl;
}