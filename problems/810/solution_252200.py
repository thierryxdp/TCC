def inverte(f):
    f2 = f.rstrip(".!?").split(",")
    f2 = ''.join(f2).split("-")
    f2 = ' '.join(f2)
    f2 = f2.lower().split()[::-1]
    return f2