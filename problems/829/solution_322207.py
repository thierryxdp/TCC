def soma_h(numero):
    lista_para_soma = []
    lista_para_numeros = list(range(1, (numero+1)))
    for num in lista_para_numeros:
        list.append(lista_para_soma, (1/num))
    soma = sum(lista_para_soma)
    return round(soma,2)