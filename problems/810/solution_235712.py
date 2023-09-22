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
    a=str.split(a)#separa as palavras
    a=list(a)#transforma em list pra poder usar o join
    a=a[::-1]
    a=str.join(' ',a)#junta as palavras separando por espaços
    return str.lower(a)#deixa udo em caixa baixa