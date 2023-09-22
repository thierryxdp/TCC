def acima_da_media(
    notas: list[float]
    ) -> list[float]:
    media = sum(notas)/len(notas)
    a = max(notas)
    list.pop(numeros,a)
    return a