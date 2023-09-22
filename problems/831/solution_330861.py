#Questão_3
def atualiza_mascara(palavrasecreta,masc,letra):
    """Atualiza a máscara, colocando a letra escolhida no seu devido lugar (caso esteja na palavra). Se a letra não estiver na palavra, a máscara deve ser retornada sem modificações. A função não ter á valor de retorno."""
    """string, list, str->int"""
    for i in range(len(palavrasecreta)):
        if palavrasecreta[i]==letra:
            masc[i]=letra
    return masc