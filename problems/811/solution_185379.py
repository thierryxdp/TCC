def colchao(s,H,L):
    "list,int,int-->bool"
    "S é referente a liste que contem as medidas do colcão da menor para maior. Já as medidas H e L sçao referentes respectivamente a altura e largura da porta"
    if s[1]<L and s[2]<H:
        return True