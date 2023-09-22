def faltante(L):
    '''Função que retorna o número pertencente ao intervalo [1,N] que já está na lista 
    list -> int'''
    list.sort(L)
    i = len(L)
    listaCerta = list(range(1,i+2))
    listaFaltantes = []
    h = 0
    while h+1<len(listaCerta):
        if L[h] != listaCerta[h]:
            return listaCerta[h]
        h = h + 1
    return listaCerta[-1]