def posLetra(s, l, n):
      ct = 0
      i = 0
      while i < len(s):
            if (s[i] == l):
                  ct += 1
                  if (ct == n):
                    return i
                    break
            i += 1
      if (n > ct):
            return -1