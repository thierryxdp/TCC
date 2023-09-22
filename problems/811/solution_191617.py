def colchao (medidas, h,l):
    if bool(sorted(medidas) < h) and bool(sorted(medidas) < l):
        return True
    if bool(sorted(medidas) > h) and bool(sorted(medidas) > l):
        return False