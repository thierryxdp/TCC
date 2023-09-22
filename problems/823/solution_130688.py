def faltante(lista):
    
    list.sort(lista)
    dado = 0
    proximo = 1
    tamanho = len(lista)
    
    if lista[0] != 1:
        return 1
    
    while proximo != tamanho:
        
        if lista[dado] != lista[proximo] - 1:
            return lista[dado] + 1
        
        if lista[proximo] == lista[-1]:
            return lista[proximo] + 1
        
        if lista[dado] == lista[proximo] - 1:
            dado += 1
            proximo += 1