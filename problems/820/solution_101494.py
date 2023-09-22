def posLetra(string,letra,n):
   """Função que recebe como entrada uma string, uma eltra e um numéro, a função deve retornar em que posição a ocorrêmcia da letra está"""
   ocorrencia = str.count(string,letra)
   ocorre =  0
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