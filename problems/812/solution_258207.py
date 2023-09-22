def retira_pontuacao (frase):
    '''função que retira a pontução de qualquer frase'''
    '''str -> str'''
    return str.join("-", str.split(frase))