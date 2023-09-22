def colchao(s,H,L):
    "list,int,int-->bool"
    "S é referente a lista que contem as medidas do colcão da menor para maior. Já as medidas H e L são referentes respectivamente a altura e largura da porta"
    "Para esta questão especificamente foi pensado que não existe(ou não deveria existir) porta mais larga que alta"
    if H<s[1] :
        "caso o colchão não passe com sua segunda maior medida na altura e sua maior medida na largura"
        return False
    else:
        return True