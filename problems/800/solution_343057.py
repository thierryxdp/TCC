def total(lista, dicio):
    listValues = []
    result = 0
    for item, value in dicio.items():
        if item in lista:
            result+= value
    return round(result,2)