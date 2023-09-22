def filtraMultiplos([],n):
    return [](filter(lambda x: (x % n), filtraMultiplos))