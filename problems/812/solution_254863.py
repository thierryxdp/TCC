def retira_pontuacao(frase):
    """calculo e retorno de uma funcao onde todos os caracteres de pontuacao sejam substituidos por espaço"""
    x=frase
    if '!':
        return str.replace(x,'.',' ')
    if ',':
        return str.replace(x,',',' ')
    if '.':
        return str.replace(x,'.',' ')