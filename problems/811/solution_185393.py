def colchao(s,H,L):
    "list,int,int-->bool"
    "S é referente a lista que contem as medidas do colcão da menor para maior. Já as medidas H e L são referentes respectivamente a altura e largura da porta"
    "Para esta questão especificamente foi pensado que não existe(ou não deveria existir) porta mais larga que alta"
    if H<s[1] and L<s[0] :
        "aqui imagin-se que o melhor jeito de passar um colchão seria com a face lateral (referente a maior medida dele), voltada para o chão"
        "imagina-se que não existe um colção de espessura suficiente pra não passar por uma porta, então o unico jeito de o colchão não passar seria se ao mesmo tempo sua segunda maior medida fosse do tamanho da altura da porta e sua maior 
        return False
    else:
        return True