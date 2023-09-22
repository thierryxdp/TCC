def quant_palavras(frase):
    """ Dada uma frase, a função retorna o número de palavras presentes na frase.
        
        Parameters:
            frase = frase a ser inserida e avaliada

        Testes:
            quant_palavras('Júlio César!') = 2
            quant_palavras('Já então namorava o piano da nossa casa, velho traste inútil, apenas de estimação.') = 14
            quant_palavras('Está na sala, penteando o cabelo, disse-me; vá devagarzinho para lhe pregar um susto.') = 14
            quant_palavras('Era o de meu pai, copiado da tela que minha mãe tinha na sala e que ainda agora está comigo.') = 20
            quant_palavras('Ainda assim, estou que aprenderia facilmente pintura, como aprendeu música mais tarde.') = 12

        Returns:
            número de palavras presentes na frase
            str --> int
    """
    lista = str.split(frase)
    numero = len(lista)
    return numero