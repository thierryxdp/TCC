def inverte(x):
    ''' Inverte a frase dada e retira as suas letras maiúsculas e pontuação. 
    str=> str '''
    if '.' or '?'or '!'or ':'or ';'or '—' or ',' in x:
        x.replace('.', ' ').replace('?',' ').replace('!',' ').replace(':',' ').replace(';',' ').replace('-',' ').replace(',',' ')
    y = x.split()
    list1=list.reverse(y)
    b=' '.join(y)
    
    return str.lower(b)