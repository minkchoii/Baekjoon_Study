#include <iostream>
using namespace std;

int main(){
    int arr[10001] = {0};
    int tmp, j;

    for(int i = 1; i <= 10000; i++){
        tmp = i;
        j = i;
        while (tmp != 0){
            j += (tmp % 10);
            tmp /= 10;
        }
        if (j <= 10000)
            arr[j] = 1;
    }
    for(int i = 1; i <= 10000; i++){
        if (arr[i] != 1){
            cout << i << "\n";
        }
    }
}
