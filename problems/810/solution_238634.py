def inverte(frase):
    '''Função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase
de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação; str-> str'''
    retira1=str.replace(frase,'-', ' ')
    retira2=str.replace(retira1, '.', ' ')
    retira3=str.replace(retira2, '!', ' ')
    retira4=str.replace(retira3, '?', ' ')
    retira5=str.replace(retira4, ':', ' ')
    retira6=str.replace(retira5, ';', ' ')
    retira7=str.replace(retira6, ',',' ')
    minusc= str.lowe(retira7)
    lista= str.split(minusc)
    inverte= lista[::-1]
    return str.join(' ', inverte)