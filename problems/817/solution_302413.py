# questão 7
import math
def acima_da_media (lista_notas):

    soma = sum(lista_notas)
    media = math.ceil(soma/ len(lista_notas))
    #calcula as médias das notas

    list.append(lista_notas,media)
    # insere a media na lista


    list.sort(lista_notas)
    # ordena os números da lista principal
    
    vazio = []
    
    if media in lista_notas:

        posicao = lista_notas.index(media)
        # retorna a posição na lista em que o elemento estará
        
        return lista_notas[posicao+1:]
    
    elif media == lista_notas:
        return lista_notas