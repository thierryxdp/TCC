def freq_palavras(text):
    '''Dado uma frase, a função retornará um dicionario onde nele estará contido as palavras presentes na frase e a quantidade de vezes que se repete.
       str->dic'''
    x=text.split(' ')
    i=0
    dic={}
    for i in range(len(x)):
        tec=text.split()
        substring=tec[i]
        text.count(substring)
        dic[tec[i]]=text.count(substring)
    i=i+1
    return dic