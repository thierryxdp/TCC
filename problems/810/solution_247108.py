def inverte(x):
    '''Esta função inverte a frase, tira a pontuação e retorna tudo em minúsculo.
str->str'''
    if '!' in x:
        x=str.replace(x,'!',' ')
    if '?' in x:
        x=str.replace(x,'?',' ')
    if '.' in x:
        x=str.replace(x,'.',' ')
    if '...' in x:
        x=str.replace(x,'...',' ')
    if ':' in x:
        x=str.replace(x,':',' ')
    if ';' in x:
        x=str.replace(x,';',' ')
    if ',' in x:
        x=str.replace(x,',',' ')
    if '-' in x:
        x=str.replace(x,'-',' ')

    y=x.split()
    list1=list.reverse(y)
    b=' '.join(y)
    
    return str.lower(b)