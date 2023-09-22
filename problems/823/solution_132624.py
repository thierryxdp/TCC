def faltante(lista):
    ''' funcao retorna o termo faltante na sequencia. list->int'''
    i=1
    a=0
    while i<=len(lista):
        if i!=int(lista[a]):
            break
        i+=1
        a+=1
    return i