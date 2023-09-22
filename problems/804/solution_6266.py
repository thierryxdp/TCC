#Start your python function here
def filtra_pares(x,y,z,w):
    """analisa os numeros e retorna somente os que sao par"""
    numero = float(input('Digite um número para saber se é par ou impar:'))
    restox = numero(x)%2
    restoy = numero(y)%2    
    restoz = numero(z)%2    
    restow = numero(w)%2 
    
    if restox,restoy,restoz,restow == 0:
        return restox,restoy,restoz,restow