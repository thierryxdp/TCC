def conta_frases(frase):
    """ Funcao que retorna o numero de frases em uma string, sendo que cada frase deve terminar com '.', '?', '!' ou '...' e só pode aparecer uma vez por frase;
      	str -> int
    """
    frase_reticencias = str.split(frase, "...")
    frase_ponto_final = str.split(str.join(frase_reticencias,''), '.')
    frase_interrogacao = str.split(str.join(frase_ponto_final), '?')
    frase_exclamacao = str.split(str.join(frase_interrogacao), '!')
    return len(frase_reticencias) + len(frase_ponto_final) + len(frase_interrogacao) + len(frase_exclamacao)