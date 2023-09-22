def posLetra(frase, letra, n):
    """Recebe uma frase, uma letra e um número, e retorna
    a posição na qual a letra de ocorrencia N aparece.
    str, str, int -> int"""
    i = 0
    contLetra = 0
    pos = 0
    while i < len(frase):
        
        if frase[i] in letra:
            contLetra += 1
            
        if contLetra == n:
           	pos = i
  
    if contLetra < n:
        return -1
    
    return pos