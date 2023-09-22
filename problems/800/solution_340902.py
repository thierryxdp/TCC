def total(lista,produtos):
    '''...'''
    
    palavras=str.split(lista)
    dic={}
    for produtos in palavras:
        if produtos in dic:
            dic=dic[produto]+1
    return dic