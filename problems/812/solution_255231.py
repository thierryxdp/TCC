def retira_pontuacao(frase):
    """calculo e retorno de uma funcao que retorna a frase sem caracteres de pontuacao e substitui por espaco"""
    x=frase
    a=str.replace(x,'.',' ') +str.replace(x,'!',' ')-x
    return a