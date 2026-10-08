print ('Bem-Vindo a minha calculadora!')
V1 = float(input('Digite o primeiro valor: '))
V2 = float(input('Digite o segundo valor: '))
Op = input('Digite a Operação: ')
Soma = V1+V2; Subtração = V1-V2; Multiplicação = V1*V2; Divisão = V1/V2

if Op in ('Soma','Mais','+','mais','soma','adição','adição'):
  print('Resultado:', Soma)
elif Op in ('Subtração','Menos','-','menos','subtração'):
  print('Resultado:', Subtração)
elif Op in ('Multiplicação','Vezes','*','vezes','multiplicação'):
  print('Resultado:', Multiplicação)
elif Op in ('Divisão','Por','/','por','divisão','dividido','Dividido'):
  print('Resultado:', Divisão)
else: print('Entrada Inválida')
