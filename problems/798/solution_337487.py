def freq_palavras(frases):
    '''
    função que recebe uma string e retorna um dicionario
    onde cada chave tem como valor o número de vezes que a
    palavra aparece
    :param frases: str
    :return: dict
    '''
    separar = frases.split()
    dicio = {}

    for palavra in separar:
       
            dicio[palavra] += 1
        else:
            dicio[palavra] = 1

	return dicio# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis