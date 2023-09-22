def busca(setor,matriz):
    '''função que dado nome de um setor e uma matriz faz a procura das informações de quais(a/o) funcionário(s/as) trabalham naquele setor. Faz uso dos laços alinhados for; setor,matriz>>>listas'''
    for c in matriz:
        for i in c:
            e= i[2]
            if setor in e:
                return i
    return []