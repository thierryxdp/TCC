def retira_pontuacao(frase):
    """ Outro jeito de fazer, só que usando join e split. Retorna a frase onde todos os caracteres de pontuaçao tenham sido substituidos por espaço;
    string->string """
    return ' '.join(re.split("[.!?,:;-]",frase))