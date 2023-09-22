def inverte(frase):
    '''função que dada uma frase retorna a mesma só que de forma invertida,e
todas as letras estarão em minúsculo.
str->str'''
    
    return str.split(retira_pontuacao(frase))[::-1]