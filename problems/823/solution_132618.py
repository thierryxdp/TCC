def faltante(lista):
    ''' funcao retorna o termo faltante na sequencia. list->int'''
    i=int(lista[0])
    while i+1<=len(lista):
        if i!=int(lista[i]):
            break
        i+=1
    return i