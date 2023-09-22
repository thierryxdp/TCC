def filtraMultiplos(lis, n):
    c = 0
    div = []
    while c != len(lis):
      if lis[c] % n == 0:
          div.append(lis[c])
          c += 1
    return div