def inverte(frase):
    '''funcao que retorna outra frase,contendo as mesmas palavras da frase de entrada na ordem inversa; str->str'''
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"_"," ")
    frase = str.replace(frase,","," ")
    frase = str.split(frase)[-1::-1]
    frase = str.join(" ",frase)
    return str.lower(frase)