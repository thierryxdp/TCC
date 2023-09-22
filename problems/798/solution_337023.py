#Questao 1
def freq_palavras(frases):
    '''
    Função que  que receba uma string e retorne um dicionário onde cada
    palavra dessa string seja uma chave e tenha como valor o  número 
    de vezes que a palavra aparece.
    str -> dic
    '''
    quant=0
    dicionario={}
    a=frases.split()
    for i in range(len(a)):
        quant=list.count(a,a[i])
        dicionario[a[i]]=quant
    return dicionario