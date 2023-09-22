def acima_da_media(notas):
        media = sum(notas)/len(notas)
        notas_acima = list()
        return ([n for n in notas if n > media])