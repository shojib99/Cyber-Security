def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_d(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))
m = int(input("Enter message: "))


if not is_prime(p) or not is_prime(q):
    print("Invalid input")
    exit()

if p == q:
    print("p and q must be different")
    exit()


n = p * q
phi = (p - 1) * (q - 1)


if e <= 1 or e >= phi or gcd(e, phi) != 1:
    print("Invalid e")
    exit()


d = find_d(e, phi)


if m < 0 or m >= n:
    print("Invalid message")
    exit()


c = pow(m, e, n)
decrypted = pow(c, d, n)


print("\nRSA RESULT")
print("n =", n)
print("phi =", phi)
print("d =", d)
print("Encrypted =", c)
print("Decrypted =", decrypted)
