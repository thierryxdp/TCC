def freq_palavras(frases):
    '''fun recebe frase e retorna dicion ́ario com
quantidade de cada palavra da string
       str--> dict'''

    palavras = frase.split()
    dict1 = {}
    counter = 0
    
    
    for elementos in palavras:
        dict1[palavras[counter]] = palavras.count(palavras[counter])
        counter += 1
        return dict1