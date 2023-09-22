def busca(setor,matriz):

    f = 0
    found_setor = []

    for i in range(len(matriz)) :

        if setor in matriz[i][2] != False:
            funci = matriz[i] 
            found_setor.append(funci)
            found_setor.remove(2)
          

    return found_setor