def pontos_por_time(lista):
    '''função que retorna um dicioário cujos mapeamentos são:<nome dotime> -> <numero total de pontos na fase'''
    a=lista[0][0]
    b=lista[0][1]
    c=lista[1][0]
    d=lista[1][1]
    if a>b:
        cormengo=3
    elif a=b:
        cormengo=1
        flamintias=1
    elif b>a:
        flamintias=3
    if d>c:
        cormengo=cormengo+3
    elif d=c:
        cormengo=cormengo+1
        flamintias=flamintias+1
    else:
        flamintias=flamintias+3
        
    tabela={Flamintias:flamintias,Cormengo:cormengo}