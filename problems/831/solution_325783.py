def lingua_p(palavra):
    """ a função recebe uma palavra em português e retorna a mesma palavra na lingua
    na lingua do P;
    str->str"""
    LP = []
    for i in range(0,len(palavra)):
        if palavra[i] in 'aeiouáéíóúâêîôû':
            list.append(LP,palavra[i]+'p'+palavra[i])
        else:
            list.append(LP,palavra[i])
    return str.join("",LP)