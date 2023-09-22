def faltante(lista):
    '''Função que dado uma lista de n-1 inteiros numerados de 1 a n,retorna o
    numero que esta falnatndo.list->int'''
    total_de_elementos=len(lista)+1
    soma_dos_elementos=total_de_elementos*(total_de_elementos+1)//2
    return soma_dos_elementos-sum(lista)