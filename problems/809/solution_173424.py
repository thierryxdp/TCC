# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def alternate_comb_nlists(*lists) -> list:
    list_itens_count = len(lists[0])
 
    for l in lists[1:]:
        assert len(l) == list_itens_count
 
    n = len(lists)
    final_length = list_itens_count * n
 
    return [lists[i % n][int(i / n)] for i in range(final_length)]