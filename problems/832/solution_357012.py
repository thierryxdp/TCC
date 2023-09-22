#list->bool
def eh_quadrada(x):
    "Função booleana que identifica se uma matriz é quadrada."
    if len(x)==len(x[0]):
        return True
    elif len(x[0])==0:
        return True
    else:
        return False