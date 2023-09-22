from math import floor

def acima_da_media(lista):
    """ Função que dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    list -> list """
    media = int(sum(lista) / len(lista))
    lista.append(media)
    lista_nov= sorted(lista)
    indM = lista_nov.index(media)
    novaLista = lista_nov[indM + 1:].copy()

    if media in lista2:
        del lista2[0]

   return lista2