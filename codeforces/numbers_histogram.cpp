#include <bits/stdc++.h>
using namespace std;

int main()
{
    char S;
    cin >> S;

    int N;
    cin >> N;

    for(int i = 0; i < N; i++)
    {
        int x;
        cin >> x;

        for(int j = 0; j < x; j++)
        {
            cout << S;
        }
        cout << '\n';
    }

    return 0;
}