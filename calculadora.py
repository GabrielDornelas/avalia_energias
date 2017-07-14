#Calculadora

def som():
	x = int(input('\nDigite o primeiro valor '))
	y = int(input('\nDigite o segundo valor '))
	print('\n', x, ' + ', y, ' = ', x + y)
	return(0)

def sub():
	x = int(input('\nDigite o primeiro valor '))
	y = int(input('\nDigite o segundo valor '))
	print('\n', x, ' - ', y, ' = ', x - y)
	return(0)

def mul():
	x = int(input('\nDigite o primeiro valor '))
	y = int(input('\nDigite o segundo valor '))
	print('\n', x, ' * ', y, ' = ', x * y)
	return(0)

def div():
	x = int(input('\nDigite o primeiro valor '))
	y = int(input('\nDigite o segundo valor '))
	print('\n', x, ' / ', y, ' = ', x / y)
	return(0)

flag = 1

while(flag == 1):
    print('Digite o caracter que deseja utilizar para conta\n')
    char = input('+ para somar, - para subtrair, * para multiplicar ou / para dividir -> ')

    if(char == '+'):
        som()
    elif(char == '-'):
        sub()
    elif(char == '*'):
        mul()
    elif(char == '/'):
        div()
    else:
        print('caracter inválido\n')
        continue

    flag = int(input('Fazer outra conta ? SIM->1 NÃO->0\n'))
