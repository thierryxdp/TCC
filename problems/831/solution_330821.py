#A funcao recebe como parametro uma palavra e retorna esta palavra traduzida
#para a lingua do P.
#p eh a palavra recebida
# string > string

def lingua_p(p):
    i = 0
    traduz = ''
    while i < len(p):
        if p[i] in 'AEIOUaeiouÁÉÍÓÚáéíóúÀà':
             traduz =  traduz + p[i] + 'p' + p[i]
        else:
             traduz =  traduz + p[i]
        i = i + 1
    return  traduz