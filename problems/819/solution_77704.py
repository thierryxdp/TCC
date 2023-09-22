def filtraMultiplos(l,n):
    """ Função que retorna todos os elementos contidos em 'l'
        list,int->list"""
    divi=[]
    ele=0
    while ele < len(l):
        if l[ele]%n == 0:
            divi += (l[ele],)
            ele += 1
            return divi