def uppCons(string):
    '''Retorna uma string com todas as consoantes maiúsculas;
    string -> string'''
    palavra = (string)
    local = 0
    while local < len(palavra):
          if palavra[local] not in 'aeiou':
             palavra[local] = str.upper(palavra[local])
             local = local + 1
          else:
              local = local + 1

    return ''.join(palavra)