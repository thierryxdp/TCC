def freq_palavras(frases):
    '''retorna um dicionario onde toda sas palvras da string frase é uma chave e tenha como valor o numero de vezes que a palavra aparece'''
    '''str -> dict'''
    
    frequencia={}
    i=0
    lista=str.split(frases)
    
    for palavra in lista:
        if lista[i] <= len(lista):
            numero=list.count(lista,palavra)
            frequencia[palavra]=numero
            i=i+1
            
    return frequencia