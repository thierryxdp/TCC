# Questão 1
def freq_palavras (frase):
    '''Retorna um dicionário com as palavras da frase e quantas vezes ela aparece na frase
    str -> dict '''
    dicionario = {}
    quais_palavras = frase.split(" ")
        # tranforma a str que recebmos como frase em lista com divisão por espaço (" ")
    vez = 0
    for palavra in quais_palavras:
        # para que a palavra estiver dentro da frase (str->list)
        lista_keys = list(dicionario.keys())
            # ele irá adicionar ao lado direito do dicionário a palavra de um dicionário vazio 
        if palavra in lista_keys:
                # se a palavra estiver no lado direito do dicionário
            dicionario[palavra] += 1
                # ele irá adicionár +1 até dar a quantidade de vezes que ela aparece na frase
        else:
            dicionario [palavra] = 1
                # se não ele adionará 1(quantidade de vezes que ela aparece)a palavra
    return dicionario