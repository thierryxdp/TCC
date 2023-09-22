def maiores(lista,n):
    """retorna uma lista que contém todos os números originais maiores que n, ordenados em ordem crescente
    list,int->list"""
   
    lista.append(n)
    lista.sort()
    lista.index(n)
    
    if len(lista)>1:
        
    	del lista[0: lista.index(n)+1]
        
    else:
    	 lista[]
    
    return lista

def acima_da_media(notas):
    """retorna uma lista ordenada com as notas que ficaram acima da média
    list->list"""
    media = sum(notas)/len(notas)
    maiores(notas,media)
    
    return notas