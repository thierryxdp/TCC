def retira_pontuacao(frase):
    """Função que retorna uma frase onde os caracteres de pontuação
    sejam substituidos por espaço
    entrada: str
    retorno: str"""
    frase= frase.replace('_', ' ')
    frase= frase.replace(',', ' ')
    frase= frase.replace(':', ' ')
    frase= frase.replace(';', ' ')
    frase= frase.replace('.', ' ')
    frase= frase.replace('?', ' ')
    frase= frase.replace('!', ' ')
    frase= frase.replace('-', ' ')
    return frase