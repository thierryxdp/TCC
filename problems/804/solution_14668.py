#Função que recebe uma tupla com quatro elementos e retorna uma nova tupla apenas com os elementos pares
#tup -> tup
def filtra_pares(t):
    if len(t)>=5:
        return "#"+t[0:2]="#"+t[3:5]+"#"