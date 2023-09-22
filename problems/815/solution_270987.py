def insere(lista_numero, n):
    ''''''
lista_numero = []
maior = menor = meio = 0
for i in range(0, 5):
    if i == 0:
        maior = menor = n
        lista_numero.append(n)
    elif n >= maior:
        maior = n
        lista_numero.append(n)
    elif n <= menor:
        menor = n
        lista_numero.insert(0, n)
    elif menor < n < maior:
        if meio == 0:
            meio = n
            lista_numero.insert(menor < n < maior, n)
        elif meio <= n:
            lista_numero.insert(meio < n < maior, n)
            meio = n
        elif meio >= n:
            lusta_numero.insert(menor < n < meio, n)
			return lista_numero