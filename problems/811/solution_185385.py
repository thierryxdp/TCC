def colchao(s,H,L):
    "list,int,int-->bool"
    "S é referente a liste que contem as medidas do colcão da menor para maior. Já as medidas H e L são referentes respectivamente a altura e largura da porta"
    if H<s[1] and L<s[2] :
        "caso o colchão não passe nem com sua segunda maior medida na altura e sua maior medida na largura"
        return False
    else:
        return True