#include <iostream>
using namespace std;

int saturating_add(int x, int y)
{
    int TMax = INT_MAX;
    int TMin = INT_MIN;
    int sum = x + y;
    int pos_overflow = (((x & TMin) == 0) + ((y & TMin) == 0) + ((sum & TMin) != 0) == 3);
    int neg_overflow = (((x & TMin) != 0) + ((y & TMin) != 0) + ((sum & TMin) == 0) == 3);
    int n1 = (-pos_overflow) & TMax;
    int n2 = (-neg_overflow) & TMin;
    int n3 = (pos_overflow - 1) & (neg_overflow - 1) & sum;
    return n1 + n2 + n3;
}


int main()
{
    cout << saturating_add(3, 4) << endl;
    cout << saturating_add(4, INT_MAX) << endl;
    cout << saturating_add(-3, INT_MIN) << endl;
    cout << saturating_add(2147483643, 483640) << endl;
    cout << saturating_add(-2147483643, -213640) << endl;
}
