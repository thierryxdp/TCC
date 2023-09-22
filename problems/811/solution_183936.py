def colchao(medidas,H,L):
    'Dada as medidas de um colchão, altura e largura da porta, retorna TRUE se o colchão passa pela porta e FALSE caso contrário. Entradas: list(int,int,int),int,int. Saída: bool.'
    area_porta=H*L
    med1=medidas[0]
    med2=medidas[1]
    med3=medidas[2]
    if med1<L and med2<H:
        return True
    if (med1*med3)<=area_porta:
        return True
    if (med3*med2)<=area_porta:
        return True
    else:
        return False