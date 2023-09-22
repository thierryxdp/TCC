def acima_da_media(notas):
    somaNotas = sum(notas)
    quantNotas = len(notas)
    mediaTurma = somaNotas / quantNotas
    novaLista = maiores(notas,mediaTurma)
    return novaLista