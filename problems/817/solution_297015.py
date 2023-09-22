def acima_da_media(notas):
    """funcao que recebe uma lista com notas dos alunos d uma turma, e retorna
    a média dos alunos da turma e uma lista ordenada com as notas que
    ficaram acima da media"""
    media = sum(notas[0])//len(notas[0])
    nota_maior=[]
    for maior in notas[0]:
        if maior > media:
            nota_maior.append(maior)
            return sorted(nota_maior)