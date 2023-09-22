def posLetra(string,letra,n):
    """Função que, dada uma string, uma letra e um número que indica a ocorrência desejada da letra, retorna em que posição da string aquela ocorrência da letra está; str,str,int->int"""
    
    ocorrencia = str.count(string,letra)
    indice = 0
    
    if 0 < n <= ocorrencia:
        
        while ocorrencia != n:
            
            if (string[indice] == letra):
                
                ocorrencia = ocorrencia-1
                
            indice = indice+1
            
    return indice
    
    elif not(0 < n <= ocorrencia):
        
        return -1