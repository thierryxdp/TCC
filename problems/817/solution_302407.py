# questão 7
import math
def acima_da_media (lista_notas):

    soma = sum(lista_notas)
    media = math.ceil(soma/ len(lista_notas))
    #calcula as médias das notas

    list.sort(lista_notas)
    # ordena os números da lista principal
    
    sucessor = media+1
    vazio = []
    
    if media in lista_notas:

        posicao = lista_notas.index(media)
        # retorna a posição na lista em que o elemento estará
        
        return lista_notas[posicao:]
    
    elif sucessor in lista_notas:
        
        posicao_sucessor = lista_notas.index(sucessor)
        # retorna a posição na lista em que o elemento estará
        
        return lista_notas[posicao_sucessor:]
    else:
        return vazio