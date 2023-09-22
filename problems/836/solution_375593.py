def busca(setor,matriz):
    trabalhadores_do_setor= []
    for trabalhador in matriz:
        if setor in trabalhador:
            trabalhadores_do_setor.append(trabalhador)