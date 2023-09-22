# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(ls,dic):
    i=0
    a=[]    
    for ls in list(dict.keys(dic)):
        a=list(dict.values(dic))
        b=sum(a)
        
        return round(b,2)