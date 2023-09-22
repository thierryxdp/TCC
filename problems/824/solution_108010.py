def uppCons(oracao):
    conso = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z","ç"]
    consoMaius = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z","Ç"]
    oracaonova = []
    v = 0
    while v < len(oracao):
        oracaonova.append(oracao[v])
        v+=1
    acumulador = 0
    a = 0
    while acumulador  < len(oracaonova):
        if oracaonova[acumulador] in conso:
            b = conso.index(oracaonova[i])
            oracaonova[acumulador] = consoMaius[b]
        acumulador+=1
    oracao = ''.join(oracaonova)
    return oracao