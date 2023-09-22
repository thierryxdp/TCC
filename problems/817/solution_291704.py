def maiores(lista,n):
    """ Dada uma lista, retorna outra com numeros maiores de n
list,int--> list"""
    lista.append(n)
    lista.sort()
    posicao= lista.index(n)
    
   
    return lista[posicao +1::]

def acima_da_media(lista):
    """Com base na funcao do exercicio 4, calcula quais alunos ficaram
acima da media.
list-->list"""
    
    n= sum(lista)//len(lista) +1 
    
   
    return maiores(lista,n)