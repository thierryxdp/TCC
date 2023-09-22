# Exercicio 5:
def insere(lista_numero, n):
    '''
    Funcao que recebe uma lista de numeros ordenados e um numero inteiro (n). A funcao retorna
    uma nova lista ordenada incluindo o novo numero (n).
    list, int -> list
    '''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero
    
# Exdercicio 6:
def maiores_que(lista_numero, n):
    '''
    Funcao que recebe uma lista de numeros ordenados e um numero inteiro (n). A funcao retorna
    uma nova lista a partir da lista original. Essa nova lista contem os numeros maiores que o numero (n).
    list, int -> list
    '''
    nova_lista_numero = insere(lista_numero, n)
    idx = nova_lista_numero.index(n)
    return nova_lista_numero[idx+1:]

# Exercicio 7:
def acima_da_meia(lista_notas):
    '''
    Funcao que recebe a lista de nota de alunos. A funcao retorna um nova lista com as notas dos alunos
    acima da media.
    list -> list
    '''
    nota_media = sum(lista_notas)/float(len(lista_notas))
    notas_acima = maiores_que(lista_notas, nota_media)
    return notas_acima