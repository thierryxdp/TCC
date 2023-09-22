def colchao(medidas,H,L):
        a = int(medidas[0])
        b = int(medidas[1])
        c = int(medidas[2])
        if H + L >= b + c:
            return "False"
        if H + L < b - c:
            return "True"