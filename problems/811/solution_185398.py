def colchao(s,H,L):
    "list,int,int-->bool"
    "S é referente a lista que contem as medidas do colcão da menor para maior. Já as medidas H e L são referentes respectivamente a altura e largura da porta"
    "Para esta questão especificamente foi pensado que não existe(ou não deveria existir) porta mais larga que alta"
    if H<s[1] and L<s[2]:
        "o colchão só não passará se a sua segunda maior medida for maior que a altura e sua maior medida for maior que a largura"
        return False
    if H<s[2] or L<s[1]:
        "o colchão só não passará se a sua segunda maior medida for maior que a altura e sua maior medida for maior que a largura"
        return False
    else:
        return True