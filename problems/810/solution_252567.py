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
    return expressao       
     

def inverte(expressao):
    b=tirar(expressao)
    a = b.split(' ')
    a.reverse() 
    return ' '.join(a)