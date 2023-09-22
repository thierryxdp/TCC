def bolos (farinha,ovos,leite):
    '''esta função calcula a quantidade máxima de bolos dados a farinha, ovos e leite
    int,int,int-->int'''
    qtd_farinha= farinha//2
    qtd_ovos= ovos//3
    qtd_leite= leite//5
    bolos=min(qtd_farinha,qtd_ovos,qtd_leite)
    return bolos