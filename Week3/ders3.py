name = "ömer tarik"
surname = "topak" 
age = "15"

print("Benim adım ",name ,surname,"yaşım ",age,"hoşgeldin")

karsilama = 'Benim adım '+ name + ' ' + surname + ' ' + 'yaşım'+ ' ' + str(age) + ' hoşgeldin'
print(karsilama)

uzunluk = len(karsilama)
print(uzunluk)

print(karsilama[3])

print(karsilama[-1])

print(karsilama[4:10])

print(karsilama[0:10])

print(karsilama[:21])

print(karsilama[11:])

print(karsilama[2:25:2])

print(karsilama[::-1])

karsilama_upper = karsilama.upper()
print(karsilama_upper)

karsilama_lower = karsilama.lower()
print(karsilama_lower)

karsilama_strip = karsilama.strip()
print(karsilama_strip)

karsilama_startwith = karsilama.startswith("e")
print(karsilama_startwith)

karsilama_split = karsilama.split()
print(karsilama_split[6])

karsilama_join = "-".join(karsilama)
print(karsilama_join)

karsilama_find = karsilama.find("ömer tarik")
print(karsilama_find)

karsilama_startwith = karsilama.startswith("A")
print(karsilama_startwith)

karsilama_endwith = karsilama.endswith("n")
print(karsilama_endwith)

karsilama_replace = karsilama.replace("ömer","Ömer")
print(karsilama_replace)





