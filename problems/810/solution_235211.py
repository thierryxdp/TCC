def inverte(a):
    #utilizando replace nas pontuações por espaços
    a=a.replace('...',' ')
    a=a.replace('.',' ')
    a=a.replace('?',' ')
    a=a.replace('!',' ')
    a=a.replace('-',' ')
    a=a.replace(',',' ')
    a=a.replace(':',' ')
    a=a.replace(';',' ')
    a=a.lower
    a=a[::-1]
    return a