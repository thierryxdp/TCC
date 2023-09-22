def faltante(lista_de_numeros):
    """funcao que, dada uma lista com n-1 elementos, todos eles em ordem, retorna o numero que falta para completar a sequencia;
    list de int -> list de int"""
    lista_em_ordem=lista_de_numeros
    list.sort(lista_em_ordem)
   
    i=0
    while i<len(lista_em_ordem):
        if not 1 in lista_em_ordem:
            return 1
        elif len(lista_em_ordem) in lista_em_ordem:
            return len(lista_em_ordem)+1
        elif lista_em_ordem[i]!=lista_completa[i]:
            i=i+1
        i=i+1
        return lista_em_ordem[i]