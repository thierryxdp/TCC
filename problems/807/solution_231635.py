def conta_frases(frases):
 	#str -> int
    
    pto_final = frases.replace("...", 'teste')
    interrogacao = pto_final.replace("!", 'teste')
    exclamacao = interrogacao.replace("?", 'teste')
    reticencias = exclamacao.replace(".", 'teste')
    return reticencias.count('teste')