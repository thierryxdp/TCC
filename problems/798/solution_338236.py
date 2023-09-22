# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dic={}
    tempdic={}
    i=0
    palavra = str.split(frases,' ')
    while i < 1+len(palavra):
    	if palavra[i] in dic:
        	dic[palavra[i]]+=1
        	i=i+1
        else:
            tempdic = {palavra[i]:1}
            dic.update(tempdic)
            i=i+1
    return dic