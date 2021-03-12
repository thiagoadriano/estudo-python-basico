str = " GTA mhn JbL \n\r"
digits = "1234"
print(len(str))
print(str[1])
print(str[1:5])
print(str[-1])
print(str[3:])
for i in str:
    print(i)

print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.islower())
print(str.strip())
print(str.title())
print(str.split())
print(str.find("mh"))
print(digits.isdigit())
print(str.casefold())
print(str.replace("mh", "MH"))
print(str.endswith("\r"))

print("%s foi retirado %d e seu saldo é %f" % ("Roberto", 30, 25.8))
print("Divisão é: {div}".format(div=10/5))
print("Divisão é: {:.2f}".format(10/9))
print("Muda isso", end=" e ")
print("Muda aquilo")