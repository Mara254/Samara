print('calculadora')
print('1 - adição')
print('2 - subtração')
print('3- multiplicação')
print('4 - divisão')

escolha = int(input('Informe o número da operação desejada: '))
número1 = float(input('Informe o 1° número: '))
número2 = float(input('Informe o 2° número: '))

if escolha == 1:
    print(número1 + número2)
elif escolha == 2:
    print(número1 - número2)

elif escolha == 3:
    print(número1 * número2)

else:
    if número2 != 0:
        print(número1 / número2)
    else:
        print('Operação invalida. Não é possivel dividir por 0')