def conta_frases(frases):
 	#str -> int
    #Função que conta a quantidade de frases em determinado texto a 
    #partir da contagem de intervalos separados por ponto final,
    #exclamação, interrogação e reticências
    
    pto_final = frases.replace("...", 'teste')
    interrogacao = pto_final.replace("!", 'teste')
    exclamacao = interrogacao.replace("?", 'teste')
    reticencias = exclamacao.replace(".", 'teste')
    return reticencias.count('teste')