def tirar_Minus(expressao):
    '''função que, dada uma string, retira a pontuação e torna 
    todos os caracteres minusculos
    str->str'''
	a=expressao
    a=a.replace('!','')
    a=a.replace('?','')
    a=a.replace(':','')
    a=a.replace(';','')
    a=a.replace('.','')
    a=a.replace(',','')
    a=a.replace('-',' ')
	a=a.lower()
    return a

def inverte(expressao):
    ''' função que dada uma expresão, retorna a mesma em ordem inversa'''
    b=tirar_Minus(expressao)
    a = b.split(' ')
    a.reverse() 
    return ' '.join(a)