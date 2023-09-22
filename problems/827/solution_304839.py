def qtd_divisores =(n): #Cria um set vazio
for i in range(1, int(n/2+1)): #itera de 1 até metade do valor numérico
    if n%i == 0: #testa se mod é zero.
        qtd_divisores.add(i) #anexa o valor de i ao set de divisores do primeiro numero