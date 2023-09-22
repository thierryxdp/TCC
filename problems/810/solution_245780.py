#Função Exercício Anterior
def retira_pontuacao(frase):
    """Função que dada uma frase, a retorna sem pontuações;
    str -> str"""
    nova_frase = frase.replace('.', ' ').replace(',', ' ').replace('?',' ').replace('!',' ').replace(';','  ').replace('-',' ')
    return nova_frase


def inverte(frase):
    """Função que recebe uma frase e retorna uma outra frase de entrada na ordem inversa, sem letras maiúsculas e pontuação;
    str -> str"""
    retira_pontuacao(frase)
    nova_frase = frase
    ifrase = [frase]
    return ifrase.reverse()