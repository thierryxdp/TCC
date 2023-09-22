def posLetra(texto, letra, ocorrencia):
    """Função que informa a posição da da ocorrencia desejada de uma letra , numa frase.
       Onde "texto" - é a str que será analisada;
            "letra" - é a letra que está procurando;
            "ocorrencia" - determina qual ocorrencia da letra é procurada.
       str, str, int --> int """
    count = 0
    indice = 0
    if texto.count(letra) < ocorrencia:
        return -1
    for i in texto:
        if i == letra:
            count += 1
        if count == ocorrencia:
            return indice
        indice += 1