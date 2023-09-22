def tirar(expressao):
 
    if ',' in expressao:
        return expressao.replace(',','')
    elif '.' in expressao:
        return expressao.replace('.','')
    elif '!' in expressao:
        return expressao.replace('!','')
    elif ':' in expressao:
        return expressao.replace(':','')
    elif '?' in expressao:
        return expressao.replace('?','') 
    else:
        return expressao.replace(';','') 

def inverte(expressao):
    tirar(expressao)
    a = b.split(' ')
    a.reverse() 
    return ' '.join(a)