def lingua_p(palavra):
    ''''''
    tr=[]
    for i range(0,len(palavra)):
        if palavra[i] in 'aeiouáéíóúâêîôû':
            list.append(traducao,palavra[i]+'p'+palavra[i])
        else:
            list.append(traducao,palavra[i])
    return str.join("",tr)