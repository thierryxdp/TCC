def maiores(lista_numero:list,n:int)->list:

    """ Função  que, dada uma lista de números inteiros e um núumero inteiro n,
        retorna outra lista, que contenha todos os numeros da lista origina
        maiores que n.

    """

    list.append(lista_numero,n)
    list.sort(lista_numero)
    pos = list.index(lista_numero,n)
    nova_lista = lista_numero[(pos+1):]
    return nova_lista


def acima_da_media(lista_notas:list)->list:
    
    """ Função que a partir de uma lista com notas dos alunos(lista_notas)
    	retorna outra lista com apenas as notas acima da média aritimética dessas notas
        
   
    """
    
    soma = sum(lista_notas)
    n_termos = len(lista_notas)
    media = soma/n_termos
    
    return maiores(lista_notas,media)