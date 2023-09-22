def filtraMultiplos(l,n):
    'Função que dado uma lista e um número, retorna uma lista apenas com os divisíveis desse número.'
    'list,int->list'
    
    c=0
    x=len(l)
    resultado=[]
    while c!=x:
        if (l[c]%n)==0:
            resultado=resultado+[l[c]]
        c=c+1
    return resultado