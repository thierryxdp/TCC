def acima_da_media(lista):
    '''Função que retorna a média dos alunos em ordem crescente
        nota da prova + 5 pontos de apresentação de trabalho
        media = 5
        media < 5 está abaixo da média
        list--->list'''
    notas1= lista[0]
    notas2= lista[1]
    notas3= lista[2]
    notas4 =lista[3]
    notas5 =lista[4]
    x = [notas1,notas2,notas3,notas4,notas5]
    list.sort(x)
    return x