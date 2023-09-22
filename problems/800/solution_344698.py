# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, dicio):
    lista=[]
    dicio={}
    newDic = { key: dicio[key] for key in dicio if dicio[key] != lista }
    sum = 0
    for i in round(newDic.values(),2):
           sum = sum + i
    return sum