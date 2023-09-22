"Função que recebe uma lista com as notas dos alunos e retorna a média e as notas maiores que a média. Lista -> lista"
    def acima_da_media(*notas):
        notas(7,8,9,5,5,3,10,4,4,9)
        med_notas = sum(notas[0])// len(notas[0])
        nota_maior = []
        for maior in notas:
            nota_maior.append(maior)
            return sorted(nota_maior)