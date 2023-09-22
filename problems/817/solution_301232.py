def  acima_da_media(notas):
    notas = (5,7,8,9,4)
    med_notas= (sum(notas[])//len(notas[]))
    nota_maior= []
    for maior in notas[0]:
        if maior > med_notas:
            nota_maior.append(maior)
    return  sorted(nota_maior)