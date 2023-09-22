def retira_pontuacao(frase):
    ''' Esta função retira as pontuações de uma frase, 
    substituindo-as por um espaço.
    str->str'''
    frase_nova = str.replace(frase, '.', ' ').replace(frase, ',', ' ')
    return frase_nova