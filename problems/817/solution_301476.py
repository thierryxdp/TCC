def abaixo_da_media(lista):
    '''Função que retorna a média dos alunos em ordem crescente
        nota da prova + 5 pontos de apresentação de trabalho
        media = 5
        media < 5 está abaixo da média
        list--->list'''
    notas1= lista[0]+5
    notas2= lista[1]+5
    notas3= lista[2]+5
    notas4 =lista[3]+5
    notas5 =lista[4]+5
    x = [notas1/2,notas2/2,notas3/2,notas4/2,notas5/2]
    list.sort(x)
    return x