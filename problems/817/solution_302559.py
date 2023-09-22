def acima_da_media(notas):
    soma = sum(notas)
    num_alunos= len(notas)
    media = soma/num_alunos
    list.sort(lista)
    return [i for i in notas if i > media]