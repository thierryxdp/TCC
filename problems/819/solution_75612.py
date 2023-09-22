def filtraMultiplos(l,n):
    "função que recebe uma lista e um número(n), e retorna outra lista contendo todos os números da lista original divisiveis por n.list,int->list."
    x=0
    while x<len(l):
        if l[x]%n!=0:
            l.pop(x)
        else:
            x=x+1
    return l