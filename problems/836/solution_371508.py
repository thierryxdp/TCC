def busca(setor,matriz):
    fun=[]
    for i in matriz:
        for j in i:
            if j==setor:
                fun.append(i)