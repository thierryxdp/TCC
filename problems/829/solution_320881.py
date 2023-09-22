def soma_h(n):
    #Essa função irá calcular e retornar o valor de H com os N termos
    #Entrada: Int | Saída: Int
    lista = range(n+1)
    soma = 0
    
    for count in lista:
        if count != 0:
      		  soma = soma + 1/count
    return round(soma,2)