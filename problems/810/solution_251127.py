def inverte(frase):
    '''função que dada uma frase retorna uma outra frase que 
     contenha as mesmas palavras da frase de entradada na ordem iversa,
     sem letras maiúsculas, e sem a pontuação; str -> str'''
    frase1= (retira_pontucao(frase))
    frase2= str.lower(frase1)
    lista= str.split(frase2)
    lista.reverse()
    str= frase[::-1]
    f=str.join('', lista)
    return f