def numeros(lista):
    tamanho_lista = len(lista)
    contador = 0
    maior_ocorrencia = 0
    while contador < tamanho_lista :
        if maior_ocorrencia < lista.count(contador):
            maior_ocorrencia = lista.count(contador)
        contador = contador + 1
    return maior_ocorrencia