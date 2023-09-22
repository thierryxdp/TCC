#Entrada:lista com notas 
#Analisa as notas acima da média e retorna uma lista ordenada com elas
def acima_da_media(notas:list)->list:
    media=sum(notas)/len(notas)
    return media