def uppCons(frase):
    """A função retorna todas as consoantes de uma frase
    	em maiusula.
        str-->str"""
    consoantes = 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'
    i=0
    while i < len(frase):
        i=i+1
        if consoantes in frase:
            posicao =str.index(frase,consoantes)
            str.upper(posicao)
    return frase