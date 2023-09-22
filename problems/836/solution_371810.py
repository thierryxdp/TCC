def busca(st, m):
    s = []
    for linha in range(len(m)):
        if m[linha][2]==st:
            del m[linha][2]
            list.append(s, m[linha])
    return s