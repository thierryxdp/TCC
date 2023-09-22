def substitui(s, x, i):
 '''Dado uma str s, retorna essa string com x no lugar dado i da str original '''
  '''string, int, int -> string '''
	 return s[0:i] + x + s[i + 1:]