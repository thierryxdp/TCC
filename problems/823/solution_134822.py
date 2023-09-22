#Exercício_06:
''' Essa função recbe uma lista de "N" números e indentifica um único que está faltando da sequência. '''
''' list ---> int. '''

def faltante(list_o):
    nt = len(list_o)
    n = list_o[-1]
    i=1
    list_c = []
    while i < n:
        list_c += [i, ]
        i += 1
    a=[]
    b=0
    j=0
    while j<nt:
        if list_o[j] == list_c[j]:
            b = 0
        else:
            a += [list_c[j]]
        j += 1
    r = a[0]
    return r