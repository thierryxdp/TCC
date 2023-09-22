def colchao(s,H,L):
    "list,int,int-->bool"
    "S é referente a liste que contem as medidas do colcão da menor para maior. Já as medidas H e L sçao referentes respectivamente a altura e largura da porta"
    if H<s[1]:
        return False
    if L<s[0]:
        return False
    else:
        return True