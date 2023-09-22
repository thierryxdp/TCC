def faltante(quantidade_atual):
    """Dado uma lista com o número identificados das peças atuais do quebra-cabeças
    menos uma das peças, retorna a peça faltando:
    list[1,N]-->int"""
    max_i=len(quantidade_atual)
    quantidade_atual.sort()
    i=(-1)
    while i<max_i:
        i+=1
        if i not in quantidade_atual:
            return i