# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dic={}
    tempdic={}
	for palavra in frases:
    def att_dic(palavra):
        if palavra in dic:
        dic[palavra]+=1
        else:
            tempdic = {palavra:1}
            dic.update(tempdic)
    return dic