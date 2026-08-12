#include <iostream>
using namespace std;
long long modularExponentiation(long long base, long long exp, long long mod) {
long long result = 1;
base = base % mod;
while (exp > 0) {
if (exp % 2 == 1) {
result = (result * base) % mod;
}
exp = exp / 2;
base = (base * base) % mod;
}
return result;
}
int main() {
long long p = 11;
long long q = 17;
long long n = p * q;
long long e = 7;
long long phi = (p - 1) * (q - 1);
long long d = 23;
long long m = 50;
long long c = modularExponentiation(m, e, n);
long long decrypted_m = modularExponentiation(c, d, n);
cout << "#include <iostream>" << endl;
cout << "=== RSA FULL PROCESS ===" << endl;
cout << "Original Message (m) : " << m << endl;
cout << "Encrypted Ciphertext (C): " << c << endl;
cout << "Decrypted Message (m) : " << decrypted_m << endl;
cout << "========================" << endl;
return 0;
}
