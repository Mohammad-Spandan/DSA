#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    int cursum=0,maxsum=INT_MIN;

    for(int i=0;i<n;i++)
    {
       cursum=cursum+arr[i];
       maxsum=max(cursum,maxsum);
       if(cursum < 0)
       {
          cursum=0;
       }
    }
    cout<<"Maximum subarray sum: "<<maxsum<<endl;

    return 0;
}