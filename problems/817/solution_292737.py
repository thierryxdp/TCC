def acima_da_media(*notas):


    """funcao que recebe uma lista com notas dos alunos e
    retorna a média da turma e uma lista que contém as notas que ficaram acima da media"""

    #list -> int, list

    media = sum(notas[0])//len(notas[0])
    n_maior=[]
    for maior in notas[0]:
        if maior > media:
            n_maior.append(maior)
    return sorted(n_maior)