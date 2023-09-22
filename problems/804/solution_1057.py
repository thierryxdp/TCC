def filtra_pares(x,y,z,w):
tup = [x,y,z,w]
for k in tup:
    if k%2 == 0:
        tup.append(k)

return tup