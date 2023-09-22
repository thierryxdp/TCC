def conta_frases(texto):
    '''retorna a quantidade de frsaes existentes em um texto qualquer
    nota: as frase sao separadas por ponto, ponto de exclamacao, ponto de interrogacao e tres pontos
    str -> int'''
    frases = texto.split('...')
    terminadores = ['!','.','...','?']

    while '' in frases:
        frases.remove('')

    quantidade = len(frases)

    for frase in frases:
        for terminador in terminadores:
        	for pos,char in enumerate(frase):
          		if(char == terminador):
            		quantidade += 1
    return quantidade