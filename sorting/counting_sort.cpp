#include <iostream>
#include <vector>
#include <limits>
using namespace std;

void countingSort(vector<int>& arr) {
    if (arr.empty()) return;
    int minVal = numeric_limits<int>::max();
    int maxVal = numeric_limits<int>::min();
    for (int x : arr) {
        minVal = min(minVal, x);
        maxVal = max(maxVal, x);
    }
    int range = maxVal - minVal + 1;
    vector<int> count(range);
    for (int x : arr) {
        count[x - minVal]++;
    }
    int index = 0;
    for (int i = 0; i < range; ++i) {
        while (count[i]-- > 0) {
            arr[index++] = i + minVal;
        }
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) cin >> arr[i];
    countingSort(arr);
    for (int x : arr) cout << x << " ";
    cout << '\n';
    return 0;
}
