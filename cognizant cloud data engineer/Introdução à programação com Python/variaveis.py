# Tipos de Váriaveis no Python (apenas os mais padrões)

# Inteiro (int)

# Ponto Flutuante (float)

# Textos (strings)

# Boleanos (bool)


# Operadores no Python (operadores aritiméticos)

# Soma ( + )

# Subtração ( - )

# Divisão ( / )

# Multiplicação ( * )

# Resto da Divisão ( % )


# Alguns exemplos abaixo

# Declaração das variáveis a , b , soma, subtração, multiplicação , divisão e resto

a = int(input('Entre com o primeiro valor : '))

b = int(input('Entre com o segundo valor : '))

soma = a + b

subtracao = a - b

divisao = a / b

multiplicacao = a * b

resto = a % b

# Printando na tela e convertendo o resultado para string para que seja mostrado na tela

#print('* O resultado da soma foi : ' + str(soma))
#print('')
#print('* O resultado da subtração foi : ' + str(subtracao))
#print('')
#print('* O resultado da divisão foi : ' + str(divisao))
#print('')
#print('* O resultado do resto da divisão foi : ' + str(resto))
#print('')
#print('* O resultado da multiplicação foi : ' + str(multiplicacao))
#print('')
#print('=======================================================================================')
#print('') 
# Outra forma de se mostrar o resultado na tela (a melhor opção)
print(' O resultado da soma foi : {}'.format(soma))
print('')
print(' O resultado da subtração foi : {}'.format(subtracao))
print('')
print(' O resultado da divisão foi : {}'.format(divisao))
print('')
print(' O resultado do resto da divisão foi : {}'.format(resto))
print('')
print(' O resultado da multiplicação foi : {}'.format(multiplicacao))