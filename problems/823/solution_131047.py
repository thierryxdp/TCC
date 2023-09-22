def faltante(Lista):
    '''Retorna o número da peça que
       está faltando, de acordo com
       a lista L de entrada;list->int'''
    comparacao=list(range(1,len(Lista)+2))
    faltante=0
    Lista.sort()
    indice=0
    total=len(Lista)
    while indice<total:
        if comparacao[indice]not in Lista:
            faltante+=comparacao[indice]
        indice+=1
        if comparacao[-1] not in Lista:
            f=comparacao[-1]
            return f
    return faltante