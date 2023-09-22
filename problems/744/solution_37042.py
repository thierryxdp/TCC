def hashtag(s):
    '''Essa função verifica se o tamanho da str e par ou impar.E retornauma str com # no comeco, meio e fim'''
    tamanho_string+ len(s)
    resto_string= tamamho_string%2
    if  resto_string==0:
        meio_string=-(-tamanho_string//2)+1
    else:
        meio_string=-(tamanho_string//2)
    1=list(s)
    1.insert(0,'#')
    1.insert(meio_string,'#')
    1.append('#')
    s=''.join(1)
    return s