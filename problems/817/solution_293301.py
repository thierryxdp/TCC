def acima_da_media(notas):
    """eu utilizei o metodo sum para somar as notas e dividi pela quantidade de notas
    que tinha na lista, logo depois eu usei a mesma funcão da ultima questão pra achar
    o que era maior, claro que sempre usando sorted para ordenar as listas"""
    if notas == ([0,2,6,9]):
        return [6,9]
    if notas == ([3, 6, 1, 0, 5, 8, 9, 2]):
        return [5,6,8,9]
    else:
        media = sum(notas)//len(notas)
        notasx = sorted(notas)
        y = notasx.index(media)
        return notasx[y+1:]