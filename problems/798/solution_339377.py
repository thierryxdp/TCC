# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """Conta quantidade de vezes que uma palavra aoarece em uma frase
    e retorna um dicionairo com dada palavra que se repete;
    str --> dict"""

    frases = str.split(frases)
    palavras_diferentes = []
    # Separa as frase faz um lista com todas as palavras distintas
    for palavra in frases:
        if not (palavra in palavras_diferentes):
            list.append(palavras_diferentes, palavra)

    buffer_dict = dict.fromkeys(palavras_diferentes)

    for palavra in palavras_diferentes:
        # Conta quantas palavras tem na frase e coloca no diocionario
        contador = 0
        for iii in frases:
            if palavra == iii:
                contador += 1
        buffer_dict[palavra] = contador
        

    return buffer_dict