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
    a=str.split(a)
    return a