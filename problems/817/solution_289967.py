def acima_da_media(notas):
    """essa funçao recebe as notas de alunos em formato de lista retornando as notas maiores que a media aritmetica dessa notas"""
    a=[sum(notas)/len(notas)]
    y=a[0]
    list.insert(notas,0,y)
    list.sort(notas)
    x=list.index(notas,y)
    return notas[1+x:len(notas)]