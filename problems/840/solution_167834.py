A, B, C = entrada.split()
A = int(A)
B = int(B)
C = int(C)

#realiza os testes necessarios para estabelecer o segundo maior valor
if (A > B and A < C) or (A > C and A < B):
    print A
elif (B > A and B < C) or (B > C and B < A):
    print B
else:
    print C