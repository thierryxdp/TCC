def repetido(ls):

    cont = 0
    let = 1
    igual = 0


    while let < len(ls):
        if ls[cont] == ls[let]:
            igual += 1
        cont += 1
        let += 1
    return igual