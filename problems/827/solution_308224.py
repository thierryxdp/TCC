def qtd_divisores(n):
    "recebe um número n e retorna a quantidade de divisores dele"
    lista = list(range(1,n+1))
    contagem = 0
    for numero in lista:
        if n%numero ==0:
            contagem += 1
    return contagem