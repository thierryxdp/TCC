def posLetra(frase,letra,n_ocorrenc):
    '''Esta função retorna a posição que se encontra a letra
    inserida, na frase, de acordo com o numero da sua ocorrencia (n_ocorrenc)
    dada.
    str, str, int -> str'''
    
    
    numero=str.find(frase,letra)
    
    while numero=<n_ocorrenc:
        if numero=n_ocorrenc:
            posicao=len(frase[:numero])
            
        numero=numero+1
        
    return posicao