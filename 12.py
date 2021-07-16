shaxs = {
    "ism": "Shohrux",
    "yoshi": 10,
    "o'quvchi": True
}
yil = int(input("yil:"))
shaxs["yoshi"] = shaxs["yoshi"] + yil
if shaxs["yoshi"] > 18:  # o'quvchining yoshi 18 kichik bo'lsa True 18 dan katta bo'lsa o'quvchi True o'chadi
    shaxs.pop("o'quvchi")
print(shaxs)
