# Dada uma lista com as notas de uma turma, esta função retorna uma lista 
# com ordenada as notas que ficaram acima da média.
# list -> list

def acima_da_media(lista):
    media = sum(lista)/len(lista)
    
    list.sort(lista)
    lista_nova = [lista for lista in lista if lista > media]
    
    return lista_nova