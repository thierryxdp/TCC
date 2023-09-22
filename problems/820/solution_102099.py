def posLetra(s, l, n):
  ct = 0
  for i in s:
    if (s[i] == l):
      ct += 1
      if (ct == n):
        return s[i]
        break
  if (n > ct):
        return -1