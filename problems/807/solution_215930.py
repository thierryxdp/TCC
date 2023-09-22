def conta_frases(frase):
    """ Funcao que retorna o numero de frases em uma string, sendo que cada frase deve terminar com '.', '?', '!' ou '...' e só pode aparecer uma vez por frase;
      	str -> int
    """
    num_frase = 0
    frase = frase.split(' ')

    pontos = ['...', '!', '?', '.']

    for palavra in frase:
        for ponto in pontos:
            if ponto in palavra:
                palavra = palavra.replace(ponto, '')
                num_frase += 1 
                
    return num_frase