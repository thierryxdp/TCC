def maiores(notas, n):
    """Função que ao ser informada uma lista de números inteiros
    e um número inteiro (n), retorna uma nova lista com todos os 
    numeros maiores que n.
    list, int -> list"""
    
    if n in notas:
        nova_lista = notas [:]
        list.sort (nova_lista)
        index_n = list.index (nova_lista, n)
    
        return nova_lista[index_n + 1:]
    
    else:
        lista_atualizada = notas [:]
        list.append(lista_atualizada, n)
        list.sort (lista_atualizada)
        index_n_ = list.index (lista_atualizada, n)
        
        return lista_atualizada[index_n_ + 1:]
    
    def acima_da_media (notas):
    #"""Função retorna uma lista ordenada com as notas que ficaram
    #acima da média.
    #list -> list"""
    
    media = sum(notas) / len (notas)
    notas_acima = []
    
    for maiores in notas:
        if miores > media:
            notas_acima.append(maiores)
            
    return media, list.sort(notas_acima)