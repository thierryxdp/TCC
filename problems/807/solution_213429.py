def conta_frases(text):
    """ Funcao que retorna, com base em um texto explicitado anteriormente,
    o numero de frases existente dentro do mesmo, com base na pontuação,
    exceto virgula.
    Entrada: str;
    Saida: int;
    
    Parameter:
    text: Texto para ser contado
    """
    frases = text.count('.') + text.count('?') + text.count('!') - 2 * text.count('...')
     
    return  frases