son = int(input("Son kiriting="))
for i in range(1,10):
   while True:
       print(son, "x", i, "=")
       natija = int(input(""))
       if natija == son * i:
           print("To'g'ri keyingisi")
           break
       else:
           print("xato qayta kiriting")



