import dis
def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário onde cada palavra é uma chave
    e o número de vezes que aparece é um valor.
    assinatura: string --> dict
    """
    _dict = {}
    lista=frases.split(' ')
    for i in range(len(lista)):
    	_dict.update({lista[i] : lista.count(lista[i])})