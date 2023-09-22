'''Função que recebe duas strings (a e b) e retorna a concatenação
delas no formato 'abba'. As strings devem, obrigatoriamente, ser
inseridas entre aspas (ex: 'string1','string2')
str,str -> str'''
def concatenacao(a, b):
    return a[:]+b[:]+b[:]+a[:]