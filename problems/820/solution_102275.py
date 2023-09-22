def posLetra(texto,letra,ocorrencia):
    teste_ocorrencia=0
    
    while False:
        if str.find(texto, letra, teste_ocorrencia) == -1:
        	x = -1
        elif teste_ocorrencia==ocorrencia:
        	x = str.find(texto, letra,teste_ocorrencia)
        elif str.find(texto, letra,teste_ocorrencia) != -1:
        	teste_ocorrencia+=1
            
    return x