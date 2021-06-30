# 9 - sinf 88 - bet 2 - masala

# n >= k bo'lmagunicha n va k ni input qilaveramiz
while True:
    n = int(input("n="))
    k = int(input("k="))
    if k <= n:
        break
    else:
        print(" k soni n ga teng yoki kichik bo'lsin")

# n! ni hisoblash
i = 0
nFaktorial = 1
while i < n:
    i += 1
    nFaktorial *= i

# k! ni hisoblash
i = 0
kFaktorial = 1
while i < k:
    i += 1
    kFaktorial *= i

# (n - k)! hisoblash
i = 0
nkFaktorial = 1
while i < (n - k):
    i += 1
    nkFaktorial *= i
print(nkFaktorial)

# misolni yechish
javob = nFaktorial / (kFaktorial * nkFaktorial)
print(javob)