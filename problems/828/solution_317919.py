def primo(n):
  ls = list(range(1, n + 1))
  ds = mapeia(ls, lambda x: (x, n % x == 0))
  fs = filtra(ds, lambda t: t[1])
  return len(fs) == 2