def  acima_da_media(*notas):
    "Função que recebe uma lista com as notas dos alunos e retorna a média e as notas maiores que a média. Lista -> lista"
    med_notas= sum(notas[0])//len(notas[0])
    nota_maior= []
    for maior in notas[0]:
        if maior > med_notas:
            nota_maior.append(maior)
    return sorted(nota_maior)