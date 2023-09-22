def lingua_p(palavra):
    #Deixando toda a string em caixa baixa
    palavra = str.lower(palavra)
    #Tranformando em lista
    lista = str.split(palavra)
    #Pegando cada letra da string
    for letra in lista:
        #Verificando se é vogal
        if letra in 'aeiou':
            #Definindo o indice da letra na palavra
            i = list.find(lista,letra)
            lista = lista[:i+1] + 'p' + lista[i:]
	return lista