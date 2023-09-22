def colchao (medidas, h,l):
    if sorted(medidas) <= h and sorted(medidas) <= l:
        return 'true'
    if sorted(medidas) > h and sorted(medidas) > l:
        return 'false'