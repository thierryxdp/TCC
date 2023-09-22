def posLetra(string,letra,n):
    """Minha função  recebe como entrada uma string, uma letra e um numero, e me retorna em qual posição
a ocorrencia da letra que foi passada esta localizada""""
    ocorrencia = str.count(string,letra)
    ocorre = 0
    indice = -1
    
    if n == ocorrencia:
        
        return string.rfind(letra)
    
    elif 0 < n < ocorrencia:
        
        while ocorre != n:
            
            indice = indice+1
            
            if (string[indice] == letra):
                
                ocorre = ocorre+1
        
        return indice
    
    elif not(0 < n <= ocorrencia):
        
        return -1