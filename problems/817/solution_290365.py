def acima_da_media(notas):
    for x in notas:
        a = sum(notas)/len(notas)
        if x > a:
            return x