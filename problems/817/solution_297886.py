def acima_da_media (nota):
    """Função que retorna as notas dos alunos que ficaram acima da média"""
    """lista -> lista"""
    soma = sum(nota)
    Ni = len(nota)
    media = (soma//Ni)
    list.append (nota, media)
    list.sort (nota)
    list.reverse (nota)
    i = list.index (nota, media)
    lista = nota[0:i]
    list.sort (lista)
    return lista