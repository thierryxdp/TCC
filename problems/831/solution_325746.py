def lingua_p(palavra):
    for x in list(palavra):
        if x in 'AEIOUaeiou':
            posicao = list.index(palavra,x)
            list.insert(list(palavra),posicao,'p')
            list.insert(list(palavra),posicao+1,x)
   	return palavra