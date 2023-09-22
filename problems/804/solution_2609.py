def piltra_pares (tupla):
    "calcula piltra_pares que receba uma tupla com quatro elementos inteiros como parâmetro e retorne uma nova tupla contendo apenas os elementos pares da tupla original tupla,tupla->tupla"
    guarda_pares = []
    for i in tupla:
        in i % 2 == 0:
            guarda_pares.append(i)
            return tuple (guarda_pares)