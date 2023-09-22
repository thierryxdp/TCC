def acima_da_media(lista):
    somaLista = sum(lista)
    mediaDaTurma = somaLista/len(lista)
    notasAcimaDaMedia = maiores(lista,mediaDaTurma)
    return (mediaDaTurma,notasAcimaDaMedia)