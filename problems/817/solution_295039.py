def acima_da_media(notas:list) -> list:
    """Essa função, dada uma lista com notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram acima da média"""
    
    media = sum(notas)/len(notas)
    notas_acima = maiores(notas, media)
    return notas_acima

def maiores(lista: list, n:int) -> list:
    """Essa função, dada uma lista de números e um número inteiro n, 
    retorna outra lista contendo todos os números da lista original
    maiores que n"""
    
    lista.append(n)
    lista = sorted(lista)
    i = lista.index(n)
    
    if max(lista) == n:
        return []
    
    elif min(lista) == n:
        lista.remove(n)
        return (lista)
    
    else:
        maiores = lista[i+1:]
        if n in maiores:
            maiores.remove(n)
        return (maiores)