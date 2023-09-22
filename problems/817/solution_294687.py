def maiores(lista,n):
     
        lista.append(n)
        lista.sort()
        i = lista.index(n)
        lista2 = lista[i+1:]
        rep = lista2.count(n)
        return lista2[rep:]

def acimaDaMedia(notas):
    """função que recebe uma lista com as notas dos alunos de uma turma e retorna
    uma lista ordenada com as notas que ficaram acima da média.
    list -> list"""
    media = sum(notas)/len(notas)
    return maiores(notas, media)