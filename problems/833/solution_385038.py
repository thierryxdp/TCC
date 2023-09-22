def conta_numero(numero,matriz):
    """Função que busca e retorna quantas vezes um número aparece numa lista"""
    """Int, List -> Int"""
    i = 0
    for buscal in range(0,len(matriz)):
        if buscal == numero:
            i += 1
        for buscac in range(0,len(matriz[-1])):
            if buscac == numero:
                i +=1                
    return i