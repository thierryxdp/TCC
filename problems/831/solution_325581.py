def lingua_p(palavra):
    '''função que recebe uma palavra como parâmetro, retornando a mesma
    traduzida para a língua do P; str -> str'''
    traducao=[]
    for i in range(0,len(palavra)):
        if palavra[i] in 'aeiouáéíóúâêîôû':
            list.append(traducao,palavra[i]+'p'+palavra[i])
        else:
            list.append(traducao,palavra[i])
    return str.join("",traduacao)