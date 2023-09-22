def colchao (medidas, h,l):
    if bool(int(str(sorted(medidas))) < h) and bool(int(str(sorted(medidas))) < l):
        return True
    if bool(int(str(sorted(medidas))) > h) and bool(int(str(sorted(medidas))) > l):
        return False