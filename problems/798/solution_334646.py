def freq_palavras(frase):
    '''Função que recebe uma string e retorna um dicionário
    no qual a palavra é a chave do número de vezes que ela aparece
    repetida na frase
    valor de entrada: string
    valor de saída: dicionário'''
    dicionario= {}
    for palavras in frase:
        repetidas= frase.count(palavras)
        dicionario['palavras']=repetidas
    return dicionario