def hashtag(s):
    """Função que insere '#' no início, no meio e no final da string recebida como
    parâmetro de entrada.
       str -> str"""
    return '#' + s[:len(s)//2] + '#' + s[(len(s)//2):] + '#'

#Teste 1:
#hashtag('abcd')--> '#ab#cd#'

#Teste 2:
#hashtag('abcde')--> '#ab#cde#'

#Teste 3:
#hashtag('Laiza')--> '#La#iza#'