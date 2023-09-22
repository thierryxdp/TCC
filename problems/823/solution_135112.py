def faltante(n_atuais):
    """Dado uma lista com o número identificados das peças atuais do quebra-cabeças
    menos uma das peças, retorna a peça faltando:
    list[1,N]-->int"""
    i=len(n_atuais)
    n=0
    while i>0:
        n=n_atuais[i-1]-n_atuais[i-2]
        i-=1
    return abs(n)