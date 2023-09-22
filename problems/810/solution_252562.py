def tirar(expressao):
 
    if ',' in expressao:
        expressao.replace(',','')
    elif '.' in expressao:
        expressao.replace('.','')
    elif '!' in expressao:
        expressao.replace('!','')
    elif ':' in expressao:
        expressao.replace(':','')
    elif '?' in expressao:
        expressao.replace('?','') 
    else:
        expressao.replace(';','') 

def inverte(expressao):
    tirar(expressao)
    a = expressao.split(' ')
    a.reverse() 
    return ' '.join(a)