def colchao(medidas,H,L):
    lado1,lado2,lado3=medidas[0],medidas[1],medidas[2]
    if((lado1<=L and lado2<=H)or(lado1<=H and lado2<=L))or((lado1<=L and lado3<=H)or(lado3<=L and lado1<=H))or((lado3<=L and lado2<=H)or(lado2<=L and lado3<=H))
    return True
else:
    return False