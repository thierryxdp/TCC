def faltante(lista):
    """ Para retornar o número que está faltando na sequencia, digite;
    int->int"""
    list.reverse(lista)
    n=lista[0]
    i=0
    x=0
    list.sort(lista)
    while i<n:
        x+=x
        if x!= lista[i]:
            return x
        i+=i
    return i+1