def conta_frases(texto):
    '''Conta quantas frases aparecem no texto
    str->int'''
    teste...= str.find(texto,'...')
    teste!=str.find(texto,'!')
    teste?=str.find(texto,'?')
    teste.=str.find(texto,'.')
    if teste...==-1 and teste!==-1 and teste?==-1 and not teste.==-1:
        return len(str.split(texto,'.'))
    elif teste...==-1 and teste!==-1 and not teste?==-1 and not teste.==-1:
        return len(str.split(str.split(texto,'.'),'?'))
    elif teste...==-1 and not teste!==-1 and teste?==-1 and not teste.==-1:
        return len(str.split(str.split(str.split(texto,'.'),'?'),'!'))
    elif teste...==-1 and not teste!==-1 and teste?==-1 and not teste.==-1: