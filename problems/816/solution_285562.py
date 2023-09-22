def insere(lista_numero,n):
    '''Dado um lista ordenada de números inteirios crescentes e um número inteiro n, retorna uma nova lista crescente com n contida nela
    list,int->list'''
    
    inserido=list.append(lista_numero,n)
    ordenado=list.sort(lista_numero)
    
    return lista_numero


def maiores(lista_numeric,n):
   '''Dados uma lista de números inteiros  e um número inteiro n, retorna uma nova lista, com apenas os valores da lista maiores do que n
   list,int->list'''
   insere_ordena_n=insere(lista_numeric,n)
   indice_n=list.index(lista_numeric,n)
   apenas_n_maior=lista_numeric[(indice_n):]
   
   return apenas_n_maior