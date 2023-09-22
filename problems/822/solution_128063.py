def repetidos(l):
    'Função que recebe uma lista de números e retorna quantos deles repetem o número diretamente posterior.'
    'list->int'
    
    x=len(l)
    c=0
    i=0
    while c!=x:
        if l[c]==l[c-1]:
            i=i+1
        c=c+1
    if l[0]==l[-1]:
        return i-1
    else:
        return i