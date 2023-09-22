# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(a):
    dicio=0   
    for x in a:
        dicio+=(x:list.count(x))    
    return dicio