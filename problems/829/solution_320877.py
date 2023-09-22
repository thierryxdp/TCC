def soma_h(n):
    #Essa função irá calcular e retornar o valor de H com os N termos
    #Entrada: Int | Saída: Int
    lista = range(n+1)
    soma = 0
    
    for contador in lista:
        if contador != 0:
        soma = soma +1/contador
    return round(soma,2)