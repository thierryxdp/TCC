def faltante(pecinhas):
    
    ''' Função que, dada uma lista com inteiros 
        (cada inteiro correspondente à numeração 
        de uma peça, obrigatoriamente incluindo a
        peça de maior numeração), retorna o número 
        da peça que falta.
        list -> int '''
    
    pecinhas.sort()
    
    i = 0
    falta = 0
    
    
    while i < len(pecinhas):
        
        condicao1 = pecinhas[i]+1 not in pecinhas
        condicao2 = pecinhas[i] == pecinhas[-1]
        
        if 1 not in pecinhas:
            falta = 1
        
        if condicao1 and not condicao2:
            falta = pecinhas[i] + 1 
            
        if condicao2 and falta == 0:
            falta = pecinhas[i] + 1 
            
        i = i+1
        
    return falta