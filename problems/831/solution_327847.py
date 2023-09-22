def lingua_p(palavra):
    '''funcao traduz a palavra para lingua do p. str->str'''
    lista=[]
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            lista.append(palavra[i]+'p'+palavra[i])
        else:
            lista.append(palavra[i])
    return "".join(lista)