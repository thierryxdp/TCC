def qtd_divisores = (num1): #Cria um set vazio
for i in range(1, int(num1/2+1)): #itera de 1 até metade do valor numérico
    if num1%i == 0: #testa se mod é zero.
        qtd_divisores.add(i) #anexa o valor de i ao set de divisores do primeiro numero