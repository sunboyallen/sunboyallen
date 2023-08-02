#include <iostream>
using namespace std;

int factor[20] = {7, 9, 10, 5, 8, 4, 2, 1, 6, 3};

int number18(string id)
{
    if (id.length() < 17)
        return -1;
    
    int s = 0;
    for (int i = 0; i < 17; i++)
        s += (id[i] - '0') * factor[i % 10];
    
    s = s % 11;
    s = (12 - s) % 11;
    return s;
}

int main()
{
    string id;
    cin >> id;
    int result = number18(id);
    if (result == -1)
        cout << "error" << endl;
    else if (result == 0)
        cout << "X" << endl;
    else
        cout << result << endl;
}