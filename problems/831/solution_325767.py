def lingua_p(palavra):
   	for x in list(palavra):
        if x not in 'AEIOUaeiou':
            lista.append(x)
        if x in 'AEIOUaeiou':
            posicao = list.index(palavra,x)
          	lista.append(x)
            lista.append('p')
            lista.append(x)
    return lista