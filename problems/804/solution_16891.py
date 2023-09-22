def par(numero):
    'retorna o resto igual a zero de um numero par. int-->int'
    return numero%2==0


def filtra_pares(elemento):
    "dados uma tupla com 4 elementos, retorna somente os numeros pares desta tupla.tupla-->tupla"
    pares=()
    if par(elemento[0]):
        pares=pares+(elemento[0],)
    if par(elemento[1]):
        pares=pares+(elemento[1],)
    if par(elemento[2]):
        pares=pares+(elemento[2],)
    if par(elemento[3]):
        pares=pares+(elemento[3],)
     
    return pares