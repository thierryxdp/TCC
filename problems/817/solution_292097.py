def acima_da_media (lista_notas):

    """ Para facilitar a vida dos professores na hora de saber
        quais alunos obtiveram notas acima da média, criemos
        uma função que faça exatamente isto...

        list -> list
    """

    media = sum(lista_notas)/len(lista_notas)

    notas_acima_media = []
    i=0
	
    while i < len(lista_notas):
        if lista_notas[i] > media:
            list.append(notas_acima_media,lista[i])
        i=i+1
        
    return sorted(notas_acima_media)