def maiores(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    indice = list.index(lista_numero,n)
    return lista_numero[(indice+1):]

def acima_da_media(lista_notas):
    soma_das_notas = sum(lista_notas)
    quant_de_notas = len(lista_notas)
    media_turma = soma_das_notas/quant_de_notas
    return maiores(lista_notas,media_turma)