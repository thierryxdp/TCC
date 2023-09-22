def soma_h(N):
    '''retorna a soma das fracoes com 1/H, onde H vai do 1 ao numero fornecido. o retorno é arredondado para
    2 casas decimais.
    int -> int'''
    i = 1
    lista_de_fracoes = []
    while i <= N:
        H = 1/i
        lista_de_fracoes.append(H)
        i+= 1
    return round(sum(lista_de_fracoes),2)