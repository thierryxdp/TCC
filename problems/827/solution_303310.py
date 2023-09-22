def qtd_divisores(n): #Recebe int
    i = 1
    divisores = [] #Lista de divisores de n
    while i <= n:
        if n%i == 0:
            list.append(divisores, i)
        i = i + 1
    qtd_divisores = len(divisores)
    return qtd_divisores #Retorna a quantidade de divisores de n