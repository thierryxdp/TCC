#n sera qualquer numero que o usuário escolher
n=input("Escolha um numero: ")
#caso o numero seja 0, o fatorial será 1
fatorial=1
#caso o numero seja maior que 0 sera aplicado uma formula 
if int(n)>1:
    for i in range(1, int(n)+1):
        fatorial=fatorial*i
    print("Fatorial de ", n, "é : ", fatorial)
else:
    print("Fatorial de ", n, " é :", fatorial)