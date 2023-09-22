def faltante(Lista):
    '''Retorna o número da peça que
       está faltando, de acordo com
       a lista "Lista" de entrada;list->int'''
    comparacao=list(range(1,len(Lista)))
        # lembre-se que o "len" de qualquer
        # sequencia, ja vai dar um indice
        # fora da lista, o que pode ser
        # exclusido
    Lista.sort()
    indice=0
    #pecas=len(Lista)+1
    total = len(Lista)
    while indice<total:
        
        if comparacao[indice]!=Lista[indice]:
            faltante = comparacao[indice]
            # voce ja achou sua resposta
            return faltante
        
        indice+=1 # O indice deve ser sempre
            # atualizado, independente de if
            # logo deve estar fora do if
    
    # Ideal seria completar a funcak, caso
    # nao haja o "faltante"
    return "Nao estao faltando pecas"
    
    # So mantendo a estrutura de terminar a 
    # funcak com return