def retira_pontuacao(frase):
    '''função que dada uma frase retorna-a sem nenhum 
    caractere de pontuação, mas com espaço em suas respectivas
    posições.
    str ->str'''
    frase_substituida = frase.replace('?',' ') and frase_substituida =frase.replace('.',' ')
    return frase_substituida