def freq_palavras(frases):
    '''função que recebe uma frase e retorna um dicionário 
    onde cada palavra dessa string seja uma chave e tenha como
    valor o numero de vezes que a palavra aparece 
    str->dicionario'''
	ocorrencia = {}
    palavras = str.split(' ')
    for palavra in palavras:
        ocorrencia[palavra] = {list.count(palavras,palavra)}
    return ocorrencia