#include <iostream>
#include <string>
using namespace std;

const char alphabet[] =
    "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF";
const char alphabet_tr[] =
    "*************************************************"
    "\r\x0c.\x1f+\x12(\x1c\x05*******6\x14\x0f\x08\'9-$*&3*14*5"
    "\x07\x04\t2\n,\"\x06\x19\x01******\x1a\0358\x03\x18\x00/\x1b"
    "\x16)\x10*\x0b%\x02#\x15\x11!\0360\0277 \x0e\x13";

unsigned long long bv2av(const char bv[13])
{
    return(
        alphabet_tr[bv[11]] +
        alphabet_tr[bv[10]] * 58ull +
        alphabet_tr[bv[ 3]] * 3364ull +
        alphabet_tr[bv[ 8]] * 195112ull +
        alphabet_tr[bv[ 4]] * 11316496ull +
        alphabet_tr[bv[ 6]] * 656356768ull - 0x2084007c0ull
    ) ^ 0x0a93b324ull;
}

char* av2bv(unsigned long long av, char bv[13])
{
    bv[0] = 'B'; bv[1] = 'V';
    bv[2] = '1'; bv[5] = '4'; bv[7] = '1'; bv[9] = '7';
    
    av = (av ^ 0x0a93b324ull) + 0x2084007c0ull;
    bv[11] = alphabet[av            % 58ull];
    bv[10] = alphabet[(av /= 58ull) % 58ull];
    bv[ 3] = alphabet[(av /= 58ull) % 58ull];
    bv[ 8] = alphabet[(av /= 58ull) % 58ull];
    bv[ 4] = alphabet[(av /= 58ull) % 58ull];
    bv[ 6] = alphabet[(av /= 58ull) % 58ull];
    return bv;
}

unsigned long long av;
char bv[20];

int main()
{

    string input;
    cin >> input;

    if(input.substr(0, 2) == "av" || input.substr(0, 2) == "av")
    {
        av = stoi(input.substr(2));
        cout << av2bv(av, bv) << endl;
    }

    else if(input.substr(0, 2) == "bv" || input.substr(0, 2) == "BV")
    {
        cout << "AV" << bv2av(input.c_str()) << endl;
    }
    
    else
        return 0;
    
}
