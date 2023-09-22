# Dada uma lista com as notas de uma turma, esta função retorna uma lista 
# com ordenada as notas que ficaram acima da média.
# list -> list

def acima_da_media(lista):
    media = sum(lista)/len(lista)
    
    list.sort(lista)
    indice = list.index(lista,media)
    
    return lista[indice:]