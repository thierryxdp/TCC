def faltante(Lista):
    '''Retorna o número da peça que
       está faltando, de acordo com
       a lista L de entrada;list->int'''
    comparacao=list(range(1,len(Lista)+2))
    Lista.sort()
    indice=0
    total=len(Lista)
    while indice<total:
        if comparacao[indice]!=Lista[indice]:
            faltante=comparacao[indice]
            return faltante
        indice+=1