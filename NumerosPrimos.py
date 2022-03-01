a = int(input('Entre com um valor: '))
div = 0

for x in range(1, a + 1):
    resto = a % x
    if resto == 0:
        div = div + 1
if div == 2:
    print('O número {} é primo!'.format(a))
else:
    print('O número {} não primo!'.format(a))