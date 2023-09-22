def total(lista,produtos):
    '''...'''
    
    palavras=str.split(lista)
    dic={}
    for palavra in lista:
        if produtos in dic:
            dic=dic[produto]+1
    return dic