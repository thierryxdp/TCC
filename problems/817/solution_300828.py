def del_num (lista_numero,n):
    '''função que deleta o número da lista
    menor igual a um número n, dado uma lista e o número
    list, int-> none'''
	
    list.sort (lista_numero)
    
    if  lista_numero == []:
        return lista_numero
    elif lista_numero [0] <= n:
        del (lista_numero [0])
        del_num (lista_numero,n)
    else:
        return lista_numero

def maiores (lista_numero,n):
    '''retorna uma lista em ordem crescente com todos os números maiores que n
    dada uma lista de números e um número n
    list, int -> list)'''
    
    del_num (lista_numero,n)

    return lista_numero

def media_notas (notas):
    '''retorna a média das notas dada uma lista
    list->float'''
    
    return (sum (notas))/len (notas)
    
def acima_da_media (notas):
    '''função que retorna todas as notas que ficaram
    acima de uma média entre elas, dada uma lista de notas)'''
    
    return maiores (notas,media_notas (notas))