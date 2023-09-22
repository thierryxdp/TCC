def colchao(medidas,H,L):
        a = medidas[0]
        b = medidas[1]
        c = medidas[2]
        if H + L >= b + c:
            return "False"
        if H + L < b - c:
            return "True"