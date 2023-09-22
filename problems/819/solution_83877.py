filtraMultiplos([],n):
   list(filter(lambda x: (x % n == 0), filtraMultiplos))