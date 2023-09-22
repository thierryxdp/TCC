def acima_da_media(notas):
    soma = sum(nota)
    num_alunos= len(notas)
    media = soma/num_alunos
    return [i for i in lista if i > media]