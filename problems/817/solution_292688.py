def media(notas_da_turma):
    """Dado uma lista com as notas dos alunos de uma turma, retorna a média da turma e uma lista com as
    notas dos alunos que ficaram acima da média
    (list[int,int,...,int]--> list[float,list[int,int,...,int]])
    ou (list[int,int,...,int]--> list[float,list[]])""" """A função aceita valores negativos e/ou números
    float como entrada nas notas e calcula a média de acordo, todavia o tipo complex causa erro não execução
    da função"""
    Media_aritmetica = sum(notas_da_turma)/(len(notas_da_turma)) #nesta etapa, calculamos a média aritmética da turma
    lista_com_elemento_medio = notas_da_turma + [Media_aritmetica] #aqui, adiciona-se a média aritmética dos termos da lista original à lista com o intuito de futuramente criar a lista com os valores maiores que a média
    list.sort(lista_com_elemento_medio) #ordena-se a lista em ordem crescente
    list.reverse(lista_com_elemento_medio) #ordena-se a lista em ordem descrescente (fazemos isso pois a primeira ocorrência da média aritmética nessa lista descrescente é a última ocorrência na lista crescente)
    indice_ocorrencia_desejada_listaDecrescente = list.index(lista_com_elemento_medio,Media_aritmetica) #descobre-se a posição da primeira ocorrencia da média na lista descrescente (essa ocorrência vai ser chamada de "ocorrência desejada")
    indice_ocorrencia_desejada_listaCrescente = len(lista_com_elemento_medio) -indice_ocorrencia_desejada_listaDecrescente -1 #por meio dessa equação, calculamos o novo valor que a "ocorrência desejada" assume quando invertemos a lista decrescente de volta para uma lista ordenada de forma crescente 
    list.reverse(lista_com_elemento_medio) #aqui revertemos a lista novamente, tornando-a ordenada crescente
    lista_aprovados = lista_com_elemento_medio[indice_ocorrencia_desejada_listaCrescente+1:] #como temos o valor da última ocorrência da média na lista crescente de notas (indice_ocorrencia_desejada_listaCrescente), podemos selecionar da lista somente as notas que são maiores que a média)
    return (Media_aritmetica,lista_aprovados)