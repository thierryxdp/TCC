def conta_frases(frase):
    """ Essa função conta o número de frases que aparecem no texto inserido.
        
        Parameters:
            frase = frase a ser inserida e avaliada

        Testes:
            conta_frases('Júlio César!') = 2
            conta_frases('Já então namorava o piano da nossa casa, velho traste inútil, apenas de estimação.') = 14
            conta_frases('Está na sala, penteando o cabelo, disse-me; vá devagarzinho para lhe pregar um susto.') = 14
            conta_frases('Era o de meu pai, copiado da tela que minha mãe tinha na sala e que ainda agora está comigo.') = 20
            conta_frases('Ainda assim, estou que aprenderia facilmente pintura, como aprendeu música mais tarde.') = 12

        Returns:
            número de frases que aparecem no texto inserido
            str --> int
    """
    frase = str.replace(frase,"...",".")
    frase = str.replace(frase,"!",".")
    frase = str.replace(frase,"?",".")
    lista = str.split(frase,".")
    numero = len(lista)
    return numero