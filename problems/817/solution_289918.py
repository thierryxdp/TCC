def maiores (lista_numeros, n):
    '''Função retorna todos os números maiores que n contidos na lista de números dada.;
    list, int -> list'''
    list.append (lista_numeros, n)
    list.sort (lista_numeros)
    posicao = list.index (lista_numeros, n)
    return lista_numeros [posicao+1:]

def acima_da_media (lista_notas):
    '''Função ordena as notas que ficaram acima da média da turma.;
    list -> list'''
    media = sum (lista_notas) // len (lista_notas)
    return maiores (lista_notas, media)