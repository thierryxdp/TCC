def colchao(medidas,H,L):
    'Dada as medidas de um colchão, altura e largura da porta, retorna TRUE se o colchão passa pela porta e FALSE caso contrário. Entradas: list(int,int,int),int,int. Saída: bool.'
    area_porta=H*L
    med1=medidas[0]
    med2=medidas[1]
    med3=medidas[2]
    if (med1<L and med2<H) or (med2<L and med2<H):
        return True
     if (med1<L and med3<H) or (med3<L and med1<H):
        return True
    if (med2<L and med3<H) or (med3<L and med2<H):
        return True
    else:
        return False