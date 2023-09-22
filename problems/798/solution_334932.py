def freq_palavras(frase):
    '''funcao que retorna um dicionario, onde cada palavra da string de entrada
    e uma chave e tenha como valor o numero de vezes que aparece na respectiva string.
    string -> dict'''
    contagem_frase= {}
    lista_frase = str.split(frase)
    for palavras in lista_frase:
        frequencia = str.count(frase, palavras)
        contagem_frase[palavras]=frequencia
    return contagem_frase