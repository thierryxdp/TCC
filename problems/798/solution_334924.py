def freq_palavras(frases):
    '''funcao que retorna um dicionario, onde cada palavra da string de entrada
    e uma chave e tenha como valor o numero de vezes que aparece na respectiva string.
    string -> dict'''
    contagem_frase= {}
    lista_frase = str.split(frases)
    for palavras in lista_frases:
        frequencia = str.count(frases, palavras)
        contagem_frase += {palavras:frequencia}
    return contagem_frase