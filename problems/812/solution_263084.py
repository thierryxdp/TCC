def retira_pontuacao(frase):
    """função que receba uma frase e retorne a frase sem a(as) pontuação(pontuações:'-', ' , ', ':', ';','!',"?","."),ou seja,a pontuação 
    foi substituida por espaço
    str->str"""
    frase=frase.replace('.',' ').replace(',',' ').replace(':',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ')
    return frase