def conta_frases(numFrases):
 '''uma funcao que canta os numeros...'''
    
    b = str.join('.',str.split(numFrases, '...')
    a = str.join('.',str.split(b, '?'))
    c = str.join('.',str.split(a, '!'))
    solucao=str.count(c,".")
    return solucao