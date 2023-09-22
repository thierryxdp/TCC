# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dic={}
    tempdic={}
    def att_dic(key):
        if key in dic:
        dic[key]+=1
        else:
            tempdic = {key:1}
            dic.update(tempdic)
    return dic