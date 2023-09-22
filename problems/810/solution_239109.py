def inverte(frase):
    """Função que dada uma 'frase', retorna uma outra frase que contenha as mesmas palavras
    da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação; str -> str """

    termo1 = str.replace(frase,"-"," ")
    termo2 = str.replace(termo1,":"," ")
    termo3 = str.replace(termo2,";"," ")
    termo4 = str.replace(termo3,"?"," ")
    termo5 = str.replace(termo4,"!"," ")
    termo6 = str.replace(termo5,","," ")
    termo7 = str.replace(termo6,"."," ")

    minuscula = str.lower(termo7)
    palavras = str.split(minuscula)
    inversao = palavras[::-1]
    
    return str.join(' ',inversao)