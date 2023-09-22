def retira_pontuacao(frase):
    """A funçao recebe como entrada uma frase (string) e a retorna (string)
    com os caracteres de pontuação substituídos por espaço."""
    return (((((((frase.replace(':', ' ')).replace('.', ' ')).replace('-', ' ')).replace(';', ' ')).replace('?', ' ')).replace('...', ' ')).replace(',', ' ')).replace('!', ' ')