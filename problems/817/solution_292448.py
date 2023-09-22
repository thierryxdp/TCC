def maiores(lista, n):
    
    lista.append(n)
    lista.sort()
    inicio_contagem = lista.index(n)
    contagem_maiores= lista[inicio_contagem+1:]

    return contagem_maiores

def acima_da_media(notasTurma):
    nNotas=len(notasTurma)
    somaNotas=sum(notasTurma)
    
    mediaTurma = somaNotas/nNotas
    
    return maiores(notasTurma,mediaTurma+0.001)