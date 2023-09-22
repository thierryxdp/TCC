def inverte(s):
    '''dada uma frase, é retornada a ordem invertida das palavras
       e sem pontuacao
       str ->  str'''
    s=str.replace(s,':',' ')
    s=str.replace(s,';',' ')
    s=str.replace(s,'.',' ')
    s=str.replace(s,'!',' ')
    s=str.replace(s,'?',' ')
    s=str.replace(s,'/',' ')
    s=str.replace(s,',',' ')
    a=str.split(s,' ')
    a=list.reverse(a)
    a=str.join('',a)
    return a