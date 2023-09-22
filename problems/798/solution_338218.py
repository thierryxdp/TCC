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
 	
    att_dicionario(rs[0][0])
    att_dicionario(rs[1][0])
    att_dicionario(rs[2][0])
    att_dicionario(rs[3][0])