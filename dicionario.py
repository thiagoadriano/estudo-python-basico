dic = {
    "marlon": {"ativo": True, "email": "marlon.manganes@teste.com"},
    "darvin": {"ativo": False, "email": "darvin.manganes@teste.com"},
    "mario": {"ativo": False, "email": "mario.manganes@teste.com"},
    "cleison": {"ativo": True, "email": "cleison.manganes@teste.com"}
}

print(dic["darvin"]["ativo"])

for item in dic:
    print("%s <%s>" % (item.title(), dic[item]['email'].lower()))


for item in dic.items():
    print(item)


for item in dic.values():
    print(item)

for item in dic.keys():
    print(item)