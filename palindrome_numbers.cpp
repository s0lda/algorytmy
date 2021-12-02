#include <iostream>
using std::cin;
using std::cout;

bool isPalindrome(int x) {
    int copy_x = x, reversed = 0, remainder;
    
    while (copy_x != 0) {
        remainder = copy_x % 10;
        reversed = reversed * 10 + remainder;
        copy_x /= 10;
    }
    if (x == reversed){
        return true;
    }
    else {
        return false;
    }
}

int main() {
    int n;
    cout << "Enter number: "; cin >> n;

    if(isPalindrome(n)) {
        cout << n << " is a palindrome.";
    }
    else {
        cout << n << " is NOT a palindrome.";
    }
    return 0;
}
