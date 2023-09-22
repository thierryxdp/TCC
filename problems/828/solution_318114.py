def primo(n):
  """O número /n/ é primo se e somente se ele possui 2 divisores."""
  # Compute uma lista com os números 1, 2, ..., n.
  ls = range(1, n + 1)
  # Descubra quais deles divide o número /n/.
  ds = mapeia(ls, lambda x: n % x == 0)
  return len(ds) == 2