def busca(setor, matriz):
    trabalhadores_do_setor=[]
    for trabalhador in matriz:
        if setor in trabalhador:
            trabalhador.remove(setor)
    trabalhadores_do_setor.append(trabalhador)
    return trabalhadores_do_setor