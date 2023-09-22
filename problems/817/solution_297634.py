def acima_da_media(lista):
    '''função que retorna uma lista composta pelas notas acima da média, tendo como valor de entrada a lista composta pelas notas dos alunos,lista''' 
    x=sum(lista)
    y=len(lista)
    n=x//y
    list.append(lista,n)
    list.sort(lista)
    A=list.index(lista,n)
    B=list.count(lista,n)
    return lista[A+B:]