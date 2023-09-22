#Questao 5
def inverte(frase):
    '''
Funcao que dada uma frase retorne uma outra
frase que contenha as mesmas palavras da frase 
de entrada na ordem inversa, sem letras 
maiusculas,e sem a pontuacao.
    '''
    a = '!.,:-;?'
    for b in range(len(a)):
        frase=frase.replace(a[b],' ')
    texto=frase.lower().split()
    texto.reverse()
    invertida=' '.join(texto)
    return invertida