# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(ls,dic):
    i=0
    for ls in list(dict.keys(dic)):
        a=dict.get(dic,ls[i])
        i=i+1
		
       	b=sum(a)
        return round(b,2)