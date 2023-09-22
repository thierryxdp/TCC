def posLetra(frase,letra,numero):
	'''Função que dada uma frase, uma letra que pode estar ou não na frase e um 
	número que indica o índice de ocorrência da letra na frase caso haja, retorna
	a posição da frase em que a letra está, caso contrário, retorna -1.
	Entrada: string, string, int
	Saída: int'''
    lista = list(frase)
    contagem = 0
    posicao = 0
    if list.count(lista, letra) >= numero:
        while contagem != numero:
            if lista[posicao] == letra:
                contagem = contagem + 1
            posicao = posicao + 1
        return posicao - 1
    else:
        return -1