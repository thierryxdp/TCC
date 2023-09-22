#Start your python function here
def filtra_pares(t):
    """tuple->tuple
    a função recebe uma tupla e nos retorna somente os numeros pares presentes nela, na mesma"""
    myit=[]
    for i in t:
        if i%2==0:
            myit.append(i)
    return myit