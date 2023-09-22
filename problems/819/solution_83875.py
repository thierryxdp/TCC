def filtraMultiplos([],n):
    return list(filter(lambda x: (x % n == 0), filtraMultiplos))