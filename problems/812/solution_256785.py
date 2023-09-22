def retira_pontuacao(frase):
    """Retorna a frase dada com os caracteres de pontuação
    alterados e transformados em um espaço."""
    remove = frase.replace('-',' ')
    remove = remove.replace(',',' ')
    remove = remove.replace(':',' ')
    remove = remove.replace(';',' ')
    remove = remove.replace('!',' ')
    remove = remove.replace('?',' ')
    remove = remove.replace('...',' ')
    remove = remove.replace('.',' ')
    return remove