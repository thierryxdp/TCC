'''"Função que recebe uma lista com as notas dos alunos e retorna a média e as notas maiores que a média. Lista -> lista'''
def  acima_da_media(*notas):
    notas = (5,7,8,9,4)
    med_notas= (sum(notas[5,7,8,9,4])//len(notas[5,7,8,9,4]))
    nota_maior= []
    for maior in notas[0]:
        if maior > med_notas:
            nota_maior.append(maior)
    return  sorted(nota_maior)