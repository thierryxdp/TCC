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
        excecao1 = pecinhas[i] == pecinhas[-1]
        excecao2 = 1 not in pecinhas
        condicao1 = pecinhas[i]+1 not in pecinhas
        
        if excecao1 and not excecao2:
            falta = pecinhas[i]-1
            
        if excecao2 and not excecao1:
            falta = 1
            
        if condicao1 and not excecao1 and not excecao2:
            falta = pecinhas[i]+1
        
        i = i+1
        
    return falta