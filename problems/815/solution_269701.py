#A função recebe uma lista ordenada e um número inteiro
#Insere o número na posição correta
def insere(lista_numero:list,n:int)->list:
    """A função recebe uma lista ordenada e um número inteiro
	   Insere o número na posição correta"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero