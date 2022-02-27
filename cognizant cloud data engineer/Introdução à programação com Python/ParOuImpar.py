a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
mod_a = a % 2
mod_b = b % 2
if mod_a == 0 or mod_b == 0:
    print("Foi digitado um valor par!")
else:
    print('Foi digitado valores ímpares!')
