def posLetra(frase,letra,num):
    """..."""
    ocorrencias = 0
    contador_posicao = 0
    
    if str.count(frase,letra) >= num:
        while contador_posicao < len(frase):
            if frase[contador_posicao] == letra:
                ocorrencias = ocorrencias+1
            contador_posicao = contador_posicao + 1    
        return contador_posicao 
            
    else:
        return -1