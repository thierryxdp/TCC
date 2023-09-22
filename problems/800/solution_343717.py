# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(ls,dic):
    for ls in list(dict.keys(dic)):
        a=dict.get(ls,list(dict.keys(dic)) )
		
        b=sum(a)
        return round(b,2)