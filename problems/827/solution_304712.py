def qtd_divisores(n):
    #Função que irá calcular o número total de divisores 
    #Dado pela variável N
    #Entrada: Int | Saída: Int
    lista = range(1,n+1)
    divisores = 0
    for count in lista:
        if n % count == 0:
            divisores = divisores + 1
        return divisores