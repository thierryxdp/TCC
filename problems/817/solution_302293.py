def maiores(lista,n):
    '''recebe uma lista de numeros ordenados do maior para o menor e um numero n qualquer
    retorna apenas os numeros maiores que n
    list, float -> list'''
    lista.append(n)
    lista.sort()
    try: 
    	if lista[lista.index(n)] == lista[lista.index(n)+1]:
        	return lista[lista.index(n)+2:]
    except IndexError:
        return []
    return lista[lista.index(n)+1:]

def acima_da_media(lista):
    '''recebe uma lista com com as notas de alunos
    retorna uma lista contendo apenas as notas que ficaram acima da média
    list -> list'''
    media = sum(lista)/len(lista)
    acima = maiores(lista,media)
    return acima