def inverte(frase):
    ' str - str '
    ' Função que dada uma frase em string, retorna a frase de trás para frente.'
    return ' '.join(palavra[::-1] for palavra in frase.split())