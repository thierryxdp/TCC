filtraMultiplos(listaN,numeroN):
    """Função que recebe uma lista e um numero n e retorna uma lista com todos os numeros dividisiveis pelo numero n."""
    """lista,int->lista"""
    multiplos=[]
    i=0
    while i < len(listaN):
        if listaN[i]%numeroN==0:
            multiplos=multiplos+[numeroN]
        i=i+1
        return multiplos