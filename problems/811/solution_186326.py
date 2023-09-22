def colchao(medidas,h,l):
    medidas[0]=grossura
    medidas[1]=largura
    medidas[2]=altura
    if altura>h and largura>l:
        return false
    if grossura>largura:
        return false
    else:
        return true