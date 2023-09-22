# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dic={}
    tempdic={}
    palavra = frases.split(' ')
    for i in palavra:
    def att_dic(palavra[i]):
        if palavra[i] in dic:
        dic[palavra[i]]+=1
        else:
            tempdic = {palavra[i]:1}
            dic.update(tempdic)
    return dic