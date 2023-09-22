def fatorial(num):
    '''retorna o fatorinal do numero'''
    x=num-1
    while x>0:
        num= num*x
        x+= -1
        return num