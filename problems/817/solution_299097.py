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


def acima_da_media(notas):
	'''funçao que recebe uma lista de notas e retorna somente as que estao acima da media;
    float->float'''
    list.sort(notas)
    y = 7 in notas
    if y = True:
        x =list.index(notas,7)
        return notas[x:]
    else:
    
   	insere(notas,7)
    return maiores(notas,7)