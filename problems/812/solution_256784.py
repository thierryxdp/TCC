def retira_pontuacao(frase):
    """Retorna a frase dada com os caracteres de pontuação
    alterados e transformados em um espaço."""
    string_pontuada = frase.replace('-',' ')
    string_pontuada = string_pontuada.replace(',',' ')
    string_pontuada = string_pontuada.replace(':',' ')
    string_pontuada = string_pontuada.replace(';',' ')
    string_pontuada = string_pontuada.replace('!',' ')
    string_pontuada = string_pontuada.replace('?',' ')
    string_pontuada = string_pontuada.replace('...',' ')
    string_pontuada = string_pontuada.replace('.',' ')
    return string_pontuada