def retira_pontuacao(frase):
    """Função que retorna uma frase onde os caracteres de pontuação
    sejam substituidos por espaço
    entrada: str
    retorno: str"""
    frase.replace('_', ' ')
    frase.replace(',', ' ')
    frase.replace(':', ' ')
    frase.replace(';', ' ')
    frase.replace('.', ' ')
    return frase