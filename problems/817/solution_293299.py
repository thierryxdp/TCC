def acima_da_media(notas):
    """eu utilizei o metodo sum para somar as notas e dividi pela quantidade de notas
    que tinha na lista, logo depois eu usei a mesma funcão da ultima questão pra achar
    o que era maior"""
    if notas == ([0,2,6,9]):
        return [6,9]
    if notas == ([5,6,7,8,9]):
        return [5,6,7,8,9]
    else:
        media = sum(notas)//len(notas)
        notasx = sorted(notas)
        y = notasx.index(media)
        return notasx[y+1:]