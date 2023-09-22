def primo(n):
    count = 0
n = int(input('Número: '))
mult = 0

while mult <= n or count < 2:
mult += 1
p = n % mult
if p == 0:
count += 1
print('Multiplos ', mult)
if count <= 2:
print('Primo')
else:
print('Não é primo')