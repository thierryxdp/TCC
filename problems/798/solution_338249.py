"""Recebe uma string e retorna um dicionário no qual cada
palavra da string seja uma chave.
Assinatura: string --> dict
Testes: 
freq_palavras("alma e coração") == {"alma":1, "e":1, "coração":1)
freq_palavras("o certo é o certo") == {"o":2,"certo":2,"é":1}

"""
def freq_palavras(frases):
    dic={}
    tempdic={}
    
    palavra = frases.split(' ')
    for x in range(0,len(palavra)):
    	if palavra[x] in dic:
        	dic[palavra[x]]+=1
        	x=x+1
        else:
            tempdic = {palavra[x]:1}
            dic.update(tempdic)
            x=x+1
    return dic