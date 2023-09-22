def posLetra(frase,letra,posicao_letra):
    """Essa função recebe uma frase, uma letra e o um numero
    n que indica a ocorrência desejada da letra. str,str,int->
    int."""
    posicao = str.find(frase, letra)
    posicao2 = posicao
    lugar = 1
    primeiro = lugar
    while lugar and primeiro < posicao_letra:
        posicao2 = posicao
        posicao = str.find(frase, letra, posicao + 1, len(frase) - 1)
        primeiro = 1 if not posicao == -1 else 0
        lugar += lugar
    return posicao