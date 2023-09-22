def freq_palavras(frases):
    '''retorna um dicionario onde toda sas palvras da string frase é uma chave e tenha como valor o numero de vezes que a palavra aparece'''
    '''str -> dict'''
    
    frequencia={}
    
    for palavra in frases:
        if len(palavra) < len(frases):
            a=str.count(frases,palavra)
            frequencia[palavra]=a
            
    return frequencia