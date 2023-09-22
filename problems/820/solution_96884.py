def posLetra(frase,letra,n_ocorrenc):
    '''Esta função retorna a posição que se encontra a letra
    inserida, na frase, de acordo com o numero da sua ocorrencia (n_ocorrenc)
    dada.
    str, str, int -> str'''
    
    indice=0
    quant_letra=str.count(frase,letra)
    posicao=[]
    
    if quant_letra<n_ocorrenc:
        return -1    
    
    while indice<len(frase):
    	if frase[indice] in letra:
            posicao=posicao[indice]    	            
                    
        indice=indice+1
        
    return posicao[indice-1]