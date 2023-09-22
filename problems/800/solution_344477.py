# Coloque um comentário dizendo o que a função faz
def total(compras = [], dic = {}):
    
    cont = 0.00
    for i in compras:
        cont += dic[i]
        return round(cont,2)
# Escolha nomes elucidativos para suas variáveis