"""Recebe uma string e retorna um dicionário no qual cada
palavra da string seja uma chave.
Assinatura: string --> dict
Testes:
"""
def freq_palavras(frases):
    dic={}
    tempdic={}
    
    palavra = frases.split(' ')
    for x in range(0,len(palavra)):
    	if palavra[x] in dic:
        	dic[palavra[x]]=x+1
        	x=x+1
        else:
            tempdic = {palavra[x]:1}
            dic.update(tempdic)
            x=x+1
    return dic