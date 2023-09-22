#Start your python function here
def deteccao_de_colisoes(retangulo_1,retangulo_2):
    """Função que verifica se há colisões entre retângulos bidimensinais, dados os valores das coordenadas xs e ys dos retângulos no formato de tuplas
    tuple,tuple-> boolean"""
    x1_1= retangulo_1[0]
    y1_1= retangulo_1[1]
    x2_1= retangulo_1[2]
    y2_1= retangulo_1[3]
    x1_2= retangulo_2[0]
    y1_2= retangulo_2[1]
    x2_2= retangulo_2[2]
    y2_2= retangulo_2[3]
    if x1_1<=x1_2<=x2_1 or x1_1<=x2_2<=x2_1 or x1_2<=x1_1<=x2_2 or x1_2<=x2_1<=x2_2:
        return True
    if y1_1<=y1_2<=y2_1 or y1_1<=y2_2<=y2_1 or y1_2<=y1_1<=y2_2 or y1_2<=y2_1<=y2_2:
        return True
    else:
        return False