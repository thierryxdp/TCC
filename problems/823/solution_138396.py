def faltante(l):
    'Função que recebe uma lista de peças numeradas e retorna qual delas está faltando.'
    'list->int'
    
    list.sort(l)
    c=1
    b=len(l)
    a=0
    if l[0]!=1:
        return 1
    else:
        while c!=b:
            if ((l[c-1])+1)!=l[c]:
                a=l[c]
            c=c+1

        if (a-1)==(-1):
            return l[b]+1
        else:
            return a-1