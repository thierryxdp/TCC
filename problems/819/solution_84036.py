def filtraMultiplos(listan, n):
    listan2 = []
    c = 0
    while c < len(listan):
        if listan[c] % n == 0:
            list.append(listan2, listan[c])
        c += 1
    return listan2