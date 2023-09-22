def faltante(lista):
    '''
    função que recebe uma lista de numeros inteiros que representam as peças do quebra cabeças
    nuemradas de 1 a N. Após isso, ela retorna o numero da peça faltante para Joaozinho pedir.
    list -> int
    '''
   	list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1] < len(lista) + 1:
        return len(lista) + 1
    contador = 0
    x_peca = 0
    while contador < len(lista) - 1:
        if lista[contador + 1] - lista[contador] > 1:
            x_peca = x_peca + lista[contador] + 1
        contador = contador + 1
    return x_peca