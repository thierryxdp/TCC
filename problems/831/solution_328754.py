def lingua_p(palavra):
    lista = []
    i = 0
    while (i < len(palavra)):
        lista.append(palavra[i])
        if (lista[i] == 'a' or
        lista[i] == 'e' or
        lista[i] == 'i' or
        lista[i] == 'o' or
        lista[i] == 'u'):
            lista.append('p'+lista[i])
        i += 1
	return ''.join(lista)