def maiores(inteiros,n):
    """Função que recebe uma lista de inteiros e retorna outra apenas com os
elementos presentes na lista original maiores do que n.
    list -> list"""
    
    if n in inteiros:
        list.sort(inteiros)
        a = list.index(inteiros,n)
        b = inteiros[a+1:]

        return b

    else:
        list.append(inteiros,n)
        list.sort(inteiros)
        a = list.index(inteiros,n)
        b = inteiros[a+1:]

        return b
    
def acima_da_media(notas):
    """Função que recebe uma lista com as notas dos alunos e retorna outra lista
com as notas que estiverem acima da média.
    list -> list"""

    a = (sum(notas))/(len(notas))
    b = maiores(notas,a)

    return b