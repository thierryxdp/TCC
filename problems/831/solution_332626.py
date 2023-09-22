def lingua_p(palavra):
    '''funcao que recebe como parametro uma palavra e retorna essa mesma palavra traduzida para lingua do p
       str -> str'''
    i=0
    while i<len(palavra):
        if palavra[i] in 'aeiouAEIOU':
            palavra_nv= palavra[:i]+'p'+palavra[i]+palavra[i::]
        i=i+1
    return palavra_nv