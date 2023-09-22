#---------------------EXERCICIO 3---------------------

def insere(lista_numero, n):
    '''insere o elemento n na lista, sem que ela
    	deixe de ser crescente
       list,int -> list'''
    
    listaNova = lista_numero[:]
    list.append(listaNova,n)
    list.sort(listaNova)
    
    return listaNova