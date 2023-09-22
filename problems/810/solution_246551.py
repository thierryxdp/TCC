def inverte(frase):
    '''função que dada uma frase retorna a mesma só que de forma invertida,e
todas as letras estarão em minúsculo.
str->str'''
    vr=frase[::-1]
    return retira_pontuacao(str.lower(frase[::-1]))