def eh_quadrada(x):
    '''A partir de uma matriz 'x' escrita em forma de lista;
ex: [[0,0,0],[0,0,0],[0,0,0]]
retorna se a mesma é quadrada ou não;
considerando uma matriz vazia como quadrada;
list => bool'''
    if len(x)==0:
        return True
    elif len(x)==len(x[0]):
        return True
    else:
        return False