def acima_da_media(lista_de_notas):
    '''Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média.
       list ---> list'''
    copia = lista_de_notas[:]
    nota_media = sum(lista_de_notas) / len(lista_de_notas)
    if nota_media in lista_de_notas:
        #list.append(lista_de_notas,nota_media)
        list.sort(lista_de_notas)
        posicao = list.index(lista_de_notas,nota_media)        
        return lista_de_notas[posicao + 1::]