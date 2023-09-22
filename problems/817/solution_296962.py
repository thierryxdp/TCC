def maiores(lista,n):
    a=([i for i in lista if i > n])
    return sorted(a)

def acima_da_media(listanotas):
    '''Coloque uma lista de notas e o resultado será todas as notas que passaram acima da média da turma inteira'''
    a=sum(listanotas)
    b= len(listanotas)
    c=a/b
    return maiores(listanotas,c)