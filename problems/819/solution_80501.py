def filtraMultiplos(lista_num,n):
  ''' Fa ̧ca uma fun ̧c ̃ao para filtrar os m ́ultiplos de um n ́umero n. Sua fun ̧c ̃ao deve receber como entrada uma
lista de n ́umeros e um n ́umero, e retornar outra lista contendo todos os elementos da lista original que
forem divis ́ıveis por n.'''
lista_num = []
lista = []
for i in lista_num: 
    if i%n == 0: 
        lista.append(i)