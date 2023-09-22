def conta_frases(frase):
    """ Essa função conta o número de frases que aparecem no texto inserido.
        
        Parameters:
            frase = frase a ser inserida e avaliada

        Testes:
            conta_frases('Preciso tirar um cochilo. Meus Deus! Que horas são? Vou perder a minha aula...') = 4
            conta_frases('As curiosidades de Capitu dão para um capítulo. Eram de vária espécie, explicáveis e inexplicáveis, assim úteis como inúteis, umas graves, outras frívolas; gostava de saber tudo.') = 2
            conta_frases('No colégio onde, desde os sete anos, aprendera a ler, escrever e contar, francês, doutrina e obras de agulha, não aprendeu, por exemplo, a fazer renda; por isso mesmo, quis que prima Justina lhe ensinasse. Se não estudou latim com o Padre Cabral foi porque o padre, depois de lhe propor gracejando, acabou dizendo que latim não era língua de meninas. Capitu confessou-me um dia que esta razão acendeu nela o desejo de o saber. Em compensação, quis aprender inglês com um velho professor amigo do pai e parceiro deste ao solo, mas não foi adiante.') = 4

        Returns:
            número de frases que aparecem no texto inserido
            str --> int
    """
    frase = str.replace(frase,"...",".")
    frase = str.replace(frase,"!",".")
    frase = str.replace(frase,"?",".")
    lista = str.split(frase,".")
    numero = len(lista)
    return numero-1