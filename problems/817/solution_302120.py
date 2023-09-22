def mediaTurma(notas):
    media = sum(notas)/len(notas)
    return media, elementosMaiores(notas, media)