def filtra_pares(a1,a2,a3,a4):
 x=()
if a1&2==0:
    x=x+tuple(a1)
if a2&2==0:
    x=x+tuple(a2)
if a3&2==0:
    x=x+tuple(a3)
if a4&2==0:
    x=x+tuple(a4)
return x