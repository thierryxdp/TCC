def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
    variavel = frase.split('.')
    variavel1 = ''.join(variavel)
    variavel2 = variavel1.split(',')
    variavel3 = ''.join(variavel2)
    variavel4 = variavel3.split('!')
    return ''.join(variavel4)