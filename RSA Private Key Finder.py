# Coding with Mubeen Nawaz
# RSA Private Key Finder
p = float(input("Enter value of p: "))
q = float(input("Enter value of q: "))
e = float(input("Enter value of e: "))
print("*****************************")
def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd(b % a, a)
        return (g, x - (b // a) * y, y)
def inverse(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        print("\nInverse not exist\n")
        exit(0)
    else:
        return x % m
def private_key(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    return (n, phi_n, d)
n, phi_n, d = private_key(p, q, e)
a = ((d * e) - 1) / phi_n
print("\nValue of n:", n)
print("\nValue of Phi(n):", phi_n)
print("\nValue of a: ", a)
print("\nPrivate key (d):", d, "\n")