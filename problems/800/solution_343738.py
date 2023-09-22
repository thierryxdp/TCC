# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(ls,dic):
    i=0
    a=[]    
    for ls in list(dict.keys(dic)):
        i=i+1
        a=list(dict.values(dic))[i]
        b=sum(a)
        
        return round(b,2)