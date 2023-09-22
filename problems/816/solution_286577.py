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