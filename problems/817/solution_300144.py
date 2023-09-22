def maiores(lista, n):
    '''uma funcao que retorna uma lista contendo todos numeros inteiros maiores
    que n. lista, int -> lista'''
    nlista = []
    for numero in lista:
        if numero > n:
            list.append(nlista, numero)
    list.sort(nlista)
    return nlista

def acima_da_media(notas):
	'''uma funcao que retorna uma lista com as notas que ficaram acima da media
    de uma determinada turma lista -> lista'''
    
    corte = sum(notas)/len(notas)
    return maiores(notas,corte)