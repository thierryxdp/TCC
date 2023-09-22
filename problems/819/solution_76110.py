def filtraMultiplos(lista,num):
    '''Função que filtra em uma lista os multiplos de um numero inteiro n e retorna
    uma lista com os elementos multiplos de n. Entrada: list,int. Saída:list'''
    lista0 = []
    multiplo = 0
    while multiplo < len(lista):
        if (lista[multiplo]%num) == 0:
            lista0 = lista0+[lista[multiplo],]
        multiplo = multiplo+1
    return lista0