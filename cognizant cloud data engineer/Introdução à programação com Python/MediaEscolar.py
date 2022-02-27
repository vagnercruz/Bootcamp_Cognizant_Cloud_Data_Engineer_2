a = float(input('Primeiro Bimestre: '))
if a > 10.0 or a < 0.0:
    a = float(input('Você digitou errado. Primeiro bimestre: '))
b = float(input('Segundo Bimestre: '))
if b > 10.0 or b < 0.0:
    b = float(input('Você digitou errado. Segundo bimestre: '))
c = float(input('Terceiro Bimestre: '))
if c > 10.0 or c < 0.0:
    c = float(input('Você digitou errado. Terceiro bimestre: '))
d = float(input('Quarto Bimestre: '))
if d > 10.0 or d < 0.0:
    a = float(input('Você digitou errado. Terceiro bimestre: '))
media = (a + b + c + d) / 4
print('A média é: {}'.format(media))
if media >= 6.00:
    print('Parabéns, você passou!')
else:
    print('Que pena, você não obteve a nota média para passar, tenta na próxima!')