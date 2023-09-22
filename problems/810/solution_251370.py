def inverte(frase):
    '''
    funcao que dada uma frase, retorna outra frase que contem as
    mesmas palavras na ordem inversa, sem letras maiusculas e sem
    pontuaçao.
    :param frase: str
    :return: str
    '''
	pto_final = frase.replace('.', ' ')
    interrogacao = pto_final.replace('?', ' ')
    exclamacao = interrogacao.replace('!', ' ')
    travessao = exclamacao.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_ptos = virgula.replace(':', ' ')
    pto_virgula = dois_ptos.replace(';', ' ')
    frase_minuscula = str.lower(exclamacao)
    frase_separada = frase_minuscula.split()
    frase_invertida = frase_separada.reverse()
    return str.join(' ',frase_separada)