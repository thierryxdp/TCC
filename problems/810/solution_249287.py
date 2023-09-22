def inverte(x):
    ''' Inverte a frase dada e retira as suas letras maiúsculas e pontuação. 
    str=> str '''
    if '.'in x:
        x=str.replace(x,'.',' ')
    if '?'in x:
        x=str.replace(x,'?',' ')
    if '!'in x:
        x=str.replace(x,'!',' ')
    if '...'in x:
        x=str.replace(x,'...',' ')
    if ':'in x:
        x=str.replace(x,':',' ')
    if ';'in x:
        x=str.replace(x,';',' ')
    if ','in x:
        x=str.replace(x,',',' ')
    if '-'in x:
        x=str.replace(x,'-',' ')          
    y = x.split()
    list1=list.reverse(y)
    b=' '.join(y)    
    return str.lower(b)