def uppCons(frase):
    '''recebe uma frase, e retorna a mesma com as consoantes
    em maiusculo;
    string->string'''
    consoantes=list('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZçÇ')
    frasesep=list(frase)
    i=0
    j=0
    caps=[]
    tamanho=len(frasesep)
    while i<tamanho:
        if frasesep[i] in consoantes:
            fg=str.upper(frasesep[i])
            list.append(caps,fg)
            frasesep[i]=caps[j]
            j=j+1
        i=i+1
    return ''.join(map(str,frasesep))