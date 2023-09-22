def maiores(list_num, n):
    """Função que ao ser informada uma lista de números inteiros
    e um número inteiro (n), retorna uma nova lista com todos os 
    numeros maiores que n.
    list, int -> list"""
    
    if n in list_num:
        nova_lista = list_num [:]
        list.sort (nova_lista)
        index_n = list.index (nova_lista, n)
        return nova_lista[index_n + 1:]
    
    else:
        lista_atualizada = list_num [:]
        list.append(lista_atualizada, n)
        list.sort (lista_atualizada)
        index_n_ = list.index (lista_atualizada, n)
        return lista_atualizada[index_n_ + 1:]
    
def acima_da_media (notas):
    """Função retorna uma lista ordenada com as notas que ficaram
    acima da média.
    list -> list"""
    
    num_notas = len(notas)
    soma_notas = sum(notas)
    media = soma_notas / num_notas
    
    if media in notas:
        notas_acima = notas [:]
        list.sort (notas_acima)
        index_z = list.index (notas_acima, media) 
        return notas_acima [index_z + 1:]
    else:
        return maiores (notas, media)