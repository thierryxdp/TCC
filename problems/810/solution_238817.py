def inverte(frase):
    '''retorna uma frase que contenha as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiusculas e sem pontuação.
    str -> str'''
    
    pontuacao = frase.replace("!"," ")+frase.replace("?"," ")+
    frase.replace("."," ")+frase.replace(";"," ")+frase.replace(":"," ")+
    frase.replace(","," ")+frase.replace("-"," ")
    
    minusc = frase.lower
    
    return pontuacao.minusc