def freq_palavras(frases):
    '''funcao que recebe uma string e retorna um dicionario
    onde cada palavra dessa string seja uma chave e tenha como
    valor o numero de vezes que a palavra aparece
    string->dicionario'''
    separar_palavras=str.split(frases)
    apareceu=0
    for elementos in frases:
        if list.count(separar_palavras,elementos)==1:
            valor= 1
        if list.count(separar_palavras,elementos)>1:
            valor=apareceu
        if elementos in frases:
            apareceu=apareceu +1
    return {elementos:apareceu}