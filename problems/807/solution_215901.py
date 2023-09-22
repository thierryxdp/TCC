def conta_frases(frase):
    """ Funcao que retorna o numero de frases em uma string, sendo que cada frase deve terminar com '.', '?', '!' ou '...' e só pode aparecer uma vez por frase;
      	str -> int
    """
    num_frases = 0
    num_frases = len(str.split(frase, "..."))
  
    return num_frases