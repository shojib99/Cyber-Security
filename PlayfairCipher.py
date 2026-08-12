#include <iostream>
#include <string>
using namespace std;
char grid[5][5];
void buildSecretGrid(string key) {
string alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
string uniqueKeyText = "";
for (char c : key) {
c = toupper(c);
if (c == 'J') c = 'I';
if (isalpha(c) && uniqueKeyText.find(c) == string::npos) {
uniqueKeyText += c;
}
}
for (char c : alphabet) {
if (uniqueKeyText.find(c) == string::npos) {
uniqueKeyText += c;
}
}
int letterIndex = 0;
for (int row = 0; row < 5; row++) {
for (int col = 0; col < 5; col++) {
grid[row][col] = uniqueKeyText[letterIndex++];
}
}
}
void locateLetter(char c, int &row, int &col) {
if (c == 'J') c = 'I';
for (int i = 0; i < 5; i++) {
for (int j = 0; j < 5; j++) {
if (grid[i][j] == toupper(c)) {
row = i;
col = j;
return;
}
}
}
}
string encryptMessage(string text) {
string cleanText = "";
for (char c : text) {
if (isalpha(c)) cleanText += toupper(c);
}
string pairs = "";
for (size_t i = 0; i < cleanText.length(); i += 2) {
pairs += cleanText[i];
if (i + 1 < cleanText.length()) {
if (cleanText[i] == cleanText[i + 1]) {
pairs += 'X';
i--;
} else {
pairs += cleanText[i + 1];
}
} else {
pairs += 'X';
}
}
string secretResult = "";
for (size_t i = 0; i < pairs.length(); i += 2) {
int r1, c1, r2, c2;
locateLetter(pairs[i], r1, c1);
locateLetter(pairs[i + 1], r2, c2);
if (r1 == r2) {
secretResult += grid[r1][(c1 + 1) % 5];
secretResult += grid[r2][(c2 + 1) % 5];
} else if (c1 == c2) {
secretResult += grid[(r1 + 1) % 5][c1];
secretResult += grid[(r2 + 1) % 5][c2];
} else {
secretResult += grid[r1][c2];
secretResult += grid[r2][c1];
}
}
return secretResult;
}
int main() {
string userKey, userMessage;
cout << "Step 1: Enter a secret key word (e.g., SECRET): ";
cin >> userKey;
cin.ignore();
buildSecretGrid(userKey);
cout << "\nHere is your generated 5x5 Secret Grid:\n";
for (int i = 0; i < 5; i++) {
for (int j = 0; j < 5; j++) {
cout << grid[i][j] << " ";
}
cout << "\n";
}
cout << "--------------------------------------\n";
cout << "Step 2: Enter the secret message you want to encrypt: ";
getline(cin, userMessage);
string encrypted = encryptMessage(userMessage);
cout << "\n=== RESULTS ===\n";
cout << "Your original message: " << userMessage << "\n";
cout << "Your encrypted cipher: " << encrypted << "\n";
cout << "============================\n";
return 0;
}
