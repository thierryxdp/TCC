def inverte(frase):
    '''função que dada uma frase retorna uma outra frase que 
     contenha as mesmas palavras da frase de entradada na ordem iversa,
     sem letras maiúsculas, e sem a pontuação; str -> str'''
    frase1= (retira_pontuacao(frase))
    frase2= str.lower(f1)
    lista= str.split(frase2)
    lista.reverse()
    frase= str.join(" ", lista)
    return frase