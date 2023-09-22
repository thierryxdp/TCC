def faltante(lista_de_numeros):
    """funcao que, dada uma lista com n-1 elementos, todos eles em ordem, retorna o numero que falta para completar a sequencia;
    list de int -> list de int"""
    lista_em_ordem=lista_de_numeros
    list.sort(lista_em_ordem)
    lista_completa=[]
    n=0
    while n<len(lista_em_ordem)+1:
        lista_completa=lista_completa+[len(lista_em_ordem)+1-n]
        list.sort(lista_completa)
        n=n+1
   
    i=0
    while i<len(lista_em_ordem)-1:
        if not 1 in lista_em_ordem:
            return 1
        elif lista_em_ordem[i]!=lista_completa[i]:
            i=i+1
        i=i+1
    return lista_em_ordem[i]+1