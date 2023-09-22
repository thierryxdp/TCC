"""função que computa os numeros multiplos de um certo numero, dada uma lista com os numeros e o numero a ser comparado
list,int -> list"""

def filtraMultiplos(ls,n):
    l=[]
    for e in ls:
        if e%n==0:
            l.append(e)
    return l