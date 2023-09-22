def lingua_p(palavra):
    lista = []
    i = 0
    while (i < len(palavra)):
        lista.append(palavra[i])
        if (palavra[i] == 'a' or
        palavra[i] == 'e' or
        palavra[i] == 'i' or
        palavra[i] == 'o' or
        palavra[i] == 'u'):
            lista.append('p'+palavra[i])
        i += 1
	return ''.join(lista)