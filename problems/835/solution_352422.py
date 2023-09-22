def melhor_volta(mat):
    if len(mat) == 6 and len(mat[0]) == 10:
        bests = []
        for x in mat:
            for y in x:
                list.append(bests,min(x))
            if min(bests) in x:
                quem = list.index(mat,x) + 1
                volta = list.index(x,min(bests)) + 1
        tempo = min(bests)
    return quem,tempo,volta