def media_matriz(mtz):
    '''retorna a  média dos números da matriz mtz não vazia
    lista->float'''
    soma=0
    for lin in mtz:
        for num in lin:
        	soma+=num
    return round(soma/(len(mtz)*(len(mtz[0]))),2)