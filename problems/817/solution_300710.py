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
    indice_n=list.index(lista_numeric,n)+1
    apenas_n_maior=lista_numeric[(indice_n):]
   
    return apenas_n_maior
   
def acima_da_media(notas):
    '''Dada uma lista de notas de uma turma, retornar apenas as notas que estão acima da média da turma
   list->list'''
    soma_notas=sum(list)
    soma_elementos=len(list)
    media=soma_notas/soma_elementos
    n=media 
    resultado=maiores(notas,n)
    return resultado