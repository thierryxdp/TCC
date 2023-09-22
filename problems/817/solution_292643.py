def maiores(lista,n):
    """Cálculo de uma função que dada uma lista de números e um numero inteiro n
    retorna outra lista que contenha todos os números da lista original maiores que n.
    
    Parameters:
    lista: corresponde a lista de números inteiros
    n: corresponde a um número inteiro 
    
    Returns:
    Retorna uma lista de números maiores que n, dado que:
    list, int -> list
    """
    l1=lista[:]
    list.append(l1,n)
    list.sort(l1)
    p=list.index(l1,n)
    return l1[p+1:]
def acima_da_media(lista):
    """Cálculo de uma função que dado uma lista com as notas dos alunos de uma turma
    retorne uma lista ordenada com as notas que ficaram acima da média.
    
      Parameters:
      lista: lista com as notas dos alunos
      
      Returns:
      Retorna uma list ordenada com as notas que ficaram acima da média dado que:
      list -> list
    """
    l1=lista[:]
    media=sum(l1)/len(l1)
    if media in l1:
        list.sort(l1)
        a=list.index(l1,media)
        return l1[a+1:]
    else:
        list.append(l1,media)
        list.sort(l1)
        p=list.index(l1,media)
        return l1[p+1:]