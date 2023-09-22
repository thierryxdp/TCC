def filtraMultiplos(l,n):
    """ Função que retorna todos os elementos contidos em 'l'
        list,int->list"""
    d=[]
    e=0
    while e < len(l):
        if l[e]%n == 0:
            d += (l[e],)
            e += 1
            return d