# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dic={}
    tempdic={}
    i=0
    count=len(i)
    palavra = frases.split(' ')
    for i in palavra:
    	def att_dic(palavra[count]):
        	if palavra[count] in dic:
        		dic[palavra[count]]+=1
        		i=i+1
        	else:
            	tempdic = {palavra[count]:1}
            	dic.update(tempdic)
    return dic