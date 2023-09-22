def carros(p, c=5):
    if p>5 or p<5:
        return int(round((p/c + 0.5)))
    else:
        return int(round(p/c))