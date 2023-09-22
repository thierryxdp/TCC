def inverte(s):
    '''dada uma frase, é retornada a ordem invertida das palavras
       e sem pontuacao
       str ->  str'''
    s=str.lower(s)
    s=str.replace(s,':',' ')
    s=str.replace(s,';',' ')
    s=str.replace(s,'.',' ')
    s=str.replace(s,'!',' ')
    s=str.replace(s,'?',' ')
    s=str.replace(s,'-',' ')
    s=str.replace(s,',',' ')
    a=str.split(s,' ')
    list.reverse(a)
    b=str.join(' ',a)
    return b