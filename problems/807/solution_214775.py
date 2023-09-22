def conta_frases(frase):
    ""
    finalespaço = str.count(frases,'. ', 0, -3)
    final = str.count(frase, '.', -1)
    exclamação = str.count(frase, '!")
    interrogação = str.count(frase, '?')
    quantidadetotal = finalespaço + final + exclamação + interrogação 
    return(quantidadetotal)