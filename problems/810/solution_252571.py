def tirar(expressao):
        a=expressao.replace('!','')
        a=expressao.replace('?','')
        a=expressao.replace(':','')
        a=expressao.replace(';','')
        a=expressao.replace('.','')
        a=expressao.replace(',','')
    return a

def inverte(expressao):
    b=tirar(expressao)
    a = b.split(' ')
    a.reverse() 
    return ' '.join(a)