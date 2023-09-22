def freq_palavras(frases):
    '''retorna um dicionario onde toda sas palvras da string frase é uma chave e tenha como valor o numero de vezes que a palavra aparece'''
    '''str -> dict'''
    
    frequencia={}
    numero = len(str.split(frases))
    
    for palavra in frases:
        if palavra in frases:
            frequencia[palavra]:numero
                
        return frequencia