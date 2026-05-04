#include<bits/stdc++.h>
using namespace std;
int main()
{
     int n=5;
    int arr[n]={1,3,5,6,10};
    int target=8;
    int left=0;
    int right=n-1;
    pair<int,int>p;
    while(left<right)
    {
        int sum=arr[left]+arr[right];
        if(sum>target)
        {
            right--;
        }
        else if(sum<target)
        {
            left++;
        }
        else
        {
           p.first=left;
           p.second=right;
           break;
        }
    }
    cout<<p.first<<" "<<p.second<<endl;


}
