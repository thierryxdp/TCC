def lingua_p(palavra):
    """ dado uma palavra a função traduz a palavra para a língua do P
    a palavra retornará sempre com letra minúscula
    
    entrada-> str
    retorna-> str"""
    
    palavra= str.lower(palavra)
    vogais= 'aeiou'
    nova_palavra=''
    for i in range(len(palavra)):
        if palavra[i] not in vogais:
            nova_palavra= nova_palavra+palavra[i]
        if palavra[i] in vogais:
            nova_palavra= nova_palavra+'p'+palavra[i]+'p'
            
    return nova_palavra