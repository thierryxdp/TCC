def acima_da_media(lista_de_notas):
    '''Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média.
       list ---> list'''
    copia = lista_de_notas[:]
    nota_media = sum(lista_de_notas) / len(lista_de_notas)
    list.sort(lista_de_notas)
    list.reverse(lista_de_notas)
    maiores = maiores(lista_de_notas,nota_media)
    lista_dos_maiores = maiores(lista_de_notas,nota_media)
    list.reverse(lista_dos_maiores)
    if nota_media in copia:
        list.insert(lista_dos_maiores,0,nota_media)
    return nota_media,lista_dos_maiores