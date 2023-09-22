def colchao(medidas,h,l):
    '''retorna se o colchao de medidas A,B,C (dentro da lista medidas) consegue passar
    	pela porta de altura h e largura l;
        list,float,float->bool'''
    alturac=max(medidas[0],medidas[1],medidas[2])
    espessurac=min(medidas[0],medidas[1],medidas[2])
    medidas[0]=alturac
    medidas[2]=espessurac
    largurac=medidas[1]
    return alturac < h and largurac<l or alturac<h and espessurac<l or espessurac<h and largurac<l or largurac<h and espessurac<l