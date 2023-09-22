def acima_da_media(notas):
    for x in notas:
        a = sum(notas)/len(notas)
        notas_acima = list()
        if x > a:
            print(x)