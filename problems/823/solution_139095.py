def faltante(lista):
    """Retorna qual peça do quebra cabeça está faltando.
    list->int"""
    c=0
    f=0
    n=0
    list.sort(lista)
    soma = (((1+(len(lista)+1))*(len(lista)+1))/2)
    while c<len(lista):
        if sum(lista) != soma:
            f=(soma)-sum(lista)
        c+=1
        n+=1
    return f