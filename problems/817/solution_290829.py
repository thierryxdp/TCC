def acima_da_media(notas):
    ''' Retorna a partir de uma lista de notas, de forma ordenada, as que foram 
        maiores que as médias das mesmas.
        list -> list '''
        media = sum(notas)/len(notas)
        notas_acima = list()
        lista = ([n for n in notas if n > media])
        list.sort(lista)
        return lista