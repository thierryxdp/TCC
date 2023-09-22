def total(lista,produtos):
    '''...'''
    
    palavras=str.split(lista)
    dic={}
    for palavras in lista:
        if produtos in dic:
            dic=dic[produto]+1
    return dic