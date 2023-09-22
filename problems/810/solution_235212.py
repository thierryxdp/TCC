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
    return a