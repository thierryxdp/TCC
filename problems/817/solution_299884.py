def acima_da_media(lista):
    '''A função retornará as notas dos alunos que obtiveram grau superior a média
    da turma.
    
    lista-> lista'''
    Q = len(lista) #Quantidade de numeros que existem na lista
    Soma = sum(lista) #Soma todos os numeros da lista
    Media = Soma/Q #Calcula a média artimética da lista
    Maiores = maiores(lista,Media) #executa a função maiores, para colocar apenas os números maiores que a média em uma lista
	
    if Media in Maiores: #Caso a média seja igual a um valor dentro da lista, vamos retirar o valor da média
        list.remove(Maiores,Media)
        return Maiores
    
    else:
	return Maiores