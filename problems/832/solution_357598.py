def eh_quadrada(m):
'''Verifica se uma matriz e quadrada
list -> bool'''
    linhas = len(m)
    if linhas==0:
        return True
    return len(m[0]) == linhas or len(m[0])==0