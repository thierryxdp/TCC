def insere(lista_numero,n):
	'''funçao que recebe um lista e um numero e rotorna o numero dentro da lista em ordem;
    float,int->float'''
    list.append(lista_numero,n)
     
    list.sort(lista_numero)
    return lista_numero


def maiores(lista_numero,n):
	'''funçao que recebe uma lista e um numero e rotorna somente valores maiores que o numero;
    foat,int->float'''
    
    insere(lista_numero,n)
    
    x = list.index(lista_numero,n)
    
    return lista_numero[x+1:]