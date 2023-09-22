def lingua_P(s):
  '''...'''
  t = ''
  i = 0
  while i<len(s):
    if s[i] in 'AEIOUaeiou':
      t += s[i] + 'p' + s[i]
    else:
      t += s[i]
    i = i + 1
return t