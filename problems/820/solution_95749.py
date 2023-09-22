def posLetra(frase, letra, ocorrencia):
    posicao = 0
    vezes = 0
    quantidade_letras = frase.count(letra)
    
    if letra in frase and ocorrencia <= quantidade_letras:
        while posicao < len(frase) and vezes != ocorrencia:
            if frase[posicao] == letra:
                posicao += 1
                vezes += 1
            
            else:
                posicao +=1
                
    else:
        pass
        
    return posicao - 1