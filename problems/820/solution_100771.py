def posLetra(string,letra,n):
    """Função que, dada uma string, uma letra e um número que indica a ocorrência desejada da letra, retorna em que posição da string aquela ocorrência da letra está; str,str,int->int"""
    
    ocorrencia = str.count(string,letra)
    ocorre = str.count(string,letra)
    indice = 0
    
    if n == ocorrencia:
        
        return string.rfind(letra)
    
    elif 0 < n < ocorrencia:
        
        while ocorre != n:
            
            if (string[indice] == letra):
                
                ocorre = ocorre-1
                
            indice = indice+1
        
        return str.find(string[indice])
    
    elif not(0 < n <= ocorrencia):
        
        return -1