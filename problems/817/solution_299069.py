def maiores(n,m):
    """ Função que exclui os números, inteiros a partir de um
    número que pertence a mesma lista
    list-> list"""
    
    n.append(m)
    n1 = sorted(n)
    n2 = n1.index(m)
     
    del(n1[0:n2+1])
    return n1

def acima_da_media(lista):
    """ Função que dada uma lista com notas de alunos retorna uma lista
    com as notas no sentido crescente
    list -> list"""    
    tamanho = len(lista)
    media = int(sum(lista)//tamanho)
    lista1 = maiores(lista,media)
    lista2 = sorted(lista1)
     
    
    return   lista2[media-1::]