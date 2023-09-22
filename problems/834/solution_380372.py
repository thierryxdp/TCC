def media_matriz (matriz):
    '''função que dada uma matriz (com inte não vazia) retor
    na a média dos numeros da matriz com 2 casas deciamis;
    list->float'''
    vari=0
    vari2=0
    for i in matriz:
    	vari+= sum(i)
    	vari2+=len(i)
    return round(vari/vari2,2)