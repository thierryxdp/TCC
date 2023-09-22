# Peça Perdida
def faltante(l):
    ''' Essa função ao receber uma lista numerada de 1 a n e sem
    repetições deve indicar qual o elemento faltante na mesma;
    LIST -> INT'''
    l.sort()
    lcomp = list(range(1,(l[len(l)-1]+2)))
    i = 0
    while i in range(0, len(l)):
        if l[i] in lcomp:
            lcomp.remove(l[i])
        i += 1
    return lcomp[0]