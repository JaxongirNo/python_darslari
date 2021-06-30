a = int(input("a="))
b = int(input("b="))

i = a
if a % 2 == 0:
    pass
elif a % 2 == 1:
    i = a + 1

while i < b:
    print(i)
    i += 2