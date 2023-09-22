def colchao(medidas,H,L):
        a = int(medidas[0])
        b = int(medidas[1])
        c = int(medidas[2])
        if int(H) + int(L) >= b + c:
            return "False"
        if int(H) + int(L) < b - c:
            return "True"