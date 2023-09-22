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
        excecao1 = pecinhas[i] == pecinhas[-1]
        excecao2 = 1 not in pecinhas
        
        if condicao1:
            falta = pecinhas[i]+1
            
        if excecao1:
            falta = pecinhas[i]-1
            
        if excecao2:
            falta = 1
        
        i = i+1
        
    return falta