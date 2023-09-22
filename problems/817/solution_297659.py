def maiores(l,n):
    '''Dada uma lista com números inteiros e um n também 
    inteiro, retorna outra lista apenas com os inteiros 
    maiores que n ordenada
    list,int -> list'''
    if n not in l:
        list.append(l,n)
    list.sort(l)
    posN = list.index(l,n)
    nova = l[(posN + 1):]
    return nova

def acima_da_media(l_notas):
    '''Dada a lista de notas de uma turma, retorna outra com
    apenas as notas acima da média ordenada
    list -> list'''
    media = sum(l_notas)//len(l_notas)
    nova = maiores(l_notas,media)
    return nova