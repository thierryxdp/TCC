def colisoes(A,B):
    """A função acima recebe duas tuplas de quatro termos e identifica se há colisão
    entre os pontos das coordenadas ou não.
       tupla -> bool
       Explicação: A função interpreta os dados recebidos como cada tupla contendo dois
       pares coordenados. No plano cartesiano, a colisão é dada pela interseção das diagonais
       de cada retângulo formado pelas coordenadas."""
    if A[2]< B[0] or B[2] < A[0] or A[3] < B[1] or B[3] < A[1]:
        return False
    else:
        return True
    
#Teste 1:
#colisoes((0,0,1,1),(0,0,1,1))--> True

#Teste 2:
#colisoes((0,0,2,2),(1,1,3,3))--> True

#Teste 3:
#colisoes((0,0,1,1),(2,2,3,3)--> False

#Teste 4:
#colisoes((2,2,5,5),(3,3,5,5))--> True

#Teste 5:
#colisoes((2,2,0,0),(3,3,2,2))--> False