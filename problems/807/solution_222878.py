def conta_frases(texto):
    '''Conta quantas frases aparecem no texto
    str->int'''
    teste1=str.find(texto,'...')
    teste2=str.find(texto,'!')
    teste3=str.find(texto,'?')
    teste4=str.find(texto,'.')
    
    if teste1==-1 and teste2==-1 and teste3==-1 and not teste4==-1:
        return len(texto.split('.'))