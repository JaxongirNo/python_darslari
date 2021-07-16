shaxs = {
    "ism": "Sunnatillo",
    "yoshi": 29,
    "kasbi": "o'qituvchi",
}
# oddiy yangi element qo'shish
shaxs["millati"]="o'zbek",
print(shaxs)

shaxs["ism"] = "Shohrux"  # edni ismi Shohruhga o'zgartirildi
print(shaxs)

shaxs.update({"manzil": "Paxtakor", "tel_raqam":"943492737"})
print(shaxs)

shaxs.pop("kasbi")
print(shaxs)

talaba = {
    "ism": "Shohrux",
    "yoshi": 22,
}
yil = int(input("necha yil o'tdi:"))
talaba["yoshi"] = talaba["yoshi"] + yil  # yoshiga yosh qo'shish
print(talaba)

