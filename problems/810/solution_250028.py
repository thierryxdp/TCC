def inverte(frase):
    '''Retorna a frase de entrada na ordem inversa, sem maiúsculas
    e sem qualquer caracter de pontuação;
    str -> str'''
    frase_nova1=retira_pontuacao(frase)
    frase_nova2=str.lower(frase_nova1)
    lista_frase=str.split(frase_nova2)
    lista_frase.reverse()
    frase_nova=str.join(' ',lista_frase)
    return frase_nova