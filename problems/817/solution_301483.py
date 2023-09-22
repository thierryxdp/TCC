def acima_da_media(notas):
    "com base numa lista<notas>, retorna uma lista ordenada com apenas as notas que estão acima da média"
    passou = []
    for i in notas:
        if i >= 5:
            passou.append(i)
    passou.sort()
    return passou