def faltante (lista):
    """Função que, dada uma lista com N elementos, descubra qual está faltando
dentro do intervalo."""
    """list-->int"""
    i=0
    resultado=0
    intervalo_completo=list(range(1,len(lista)+2))
    while i<len(intervalo_completo):
        if intervalo_completo[i] not in lista:
            resultado=resultado+intervalo_completo[i]
        i=i+1
    return resultado