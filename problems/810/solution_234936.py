def inverte(frase):
    '''funcao que retorna outra frase contendo as mesmas palavras da frase de entrada na ordem inversa,sem letras maisculas,e sem pontuacao'''
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," )
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,"!,"," ")
    frase = str.replace(frase)[-1 ::-1]
    frase = str.join(" ",frase)
    return str.lower(frase)