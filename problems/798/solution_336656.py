def freq_palavras(frases):
    """funcao que recebe uma string e retorna um dicionario em que cada palavra é uma chave e contém a quatindade
    de vezes que essa palavra aparece. str -> dic"""
    resposta = {}
    contagem = 0 
    palavras = str.split(frases)
    while contagem < len(palavras):
        respostas[palavras[contagem]]=list.count(palavras,palavras[contagem])
        contagem += 1
    return resposta