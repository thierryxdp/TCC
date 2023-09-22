#Função Exercício Anterior
def retira_pontuacao(frase):
    """Função que dada uma frase, a retorna sem pontuações;
    str -> str"""
    frase = frase.replace('.', ' ').replace(',', ' ').replace('?',' ').replace('!',' ').replace(';','  ').replace('-',' ')
    return frase


def inverte(frase):
    """Função que recebe uma frase e retorna uma outra frase de entrada na ordem inversa, sem letras maiúsculas e pontuação;
    str -> str"""
    
    ifrase = [frase]
    return ifrase.reverse()