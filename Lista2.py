#-------------------------------------------------------
#Nome : Ana Paula Fernandes de Souza
#Atualização : 05/02/2018
#Lista 2
#Assunto : Tomada de Decisão
#-------------------------------------------------------


# 1) Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.


# num = float(input("Digite um numero"))
#
# if(num==0):
#     print("O numero é zero")
# elif(num<0):
#     print("O numero é negativo")
# else:
#     print("O numero é positivo")


# 2 - 7) Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.

# num = int(input("Digite um numero "))
#
# tipo= "par" if(num%2==0)  else "impar"
#
# print("O numero é ",tipo)


# 3) Faça um algoritmo que leia dois números e imprima o maior.

# num1 = float(input("Digite o primeiro numero"))
# num2 = float(input("Digite o segundo numero"))
#
# if(num1>num2):
#     print("O maior numero é ",num1)
# else:
#     print("O maior numero é ",num2)

# 4) Faça um algoritmo que peça a idade de uma pessoa e
# imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.


# idade=int(input("Digite sua idade "))
#
# if(idade<18):
#     print("Você é de menor")
# else:
#     print("Você é de maior")

# 5) Faça um algoritmo que peça a idade do usuário e a idade da sua mãe.
# Em seguida, imprima na tela com quantos anos sua mãe o teve.

# idade_mae=int(input("Digite a idade da sua mae : "))
# idade=int(input("Digite a sua idade : "))
#
# print("Sua mae te teve com ",idade_mae-idade)

# 6) Faça um algoritmo que imprima 50 vezes o caractere "-" na tela (sem a utilização de laços de repetição).

# print("-"*50)


# 8) Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.


# num1 = float(input("Digite o primeiro numero"))
# num2 = float(input("Digite o segundo numero"))

# if(num1>num2):
#     print("O maior numero é ",num1)
#     print("O menor numero é ",num2)
# else:
#     print("O maior numero é ",num2)
#     print("O menor numero é ",num1)


# 9) Faça um algoritmo que verifica se um determinado valor é um número inteiro.

# num = 5
#
# if(type(num) is int):
#    print("O numero é um inteiro")
# else:
#     print("O valor não é inteiro")

#11) Faça um algoritmo que verifica se um determinado valor é do tipo decimal.

# num = 7.5
#
# if(type(num) is int):
#    print("O numero é um decimal")
# else:
#     print("O valor não é decimal")

#12)Faça um algoritmo que peça um valor numérico. Em seguida, verifique se o número é inteiro ou decimal.







# 13) Faça um algoritmo que leia três números e imprima na tela o maior deles.


# num1 = float(input("Digite o primeiro numero"))
# num2 = float(input("Digite o segundo numero"))
# num3 = float(input("Digite o terceiro numero"))

# if(num1>=num2 and num1>=num3):
#     print("O maior numero é ",num1)
# elif(num2>=num1 and num2>=num3):
#     print("O maior numero é ",num2)
# else:
#     print("O maior numero é ",num3)

# 14) Faça um algoritmo que leia três números e imprima-os em ordem crescente.

# num1 = float(input("Digite o primeiro numero"))
# num2 = float(input("Digite o segundo numero"))
# num3 = float(input("Digite o terceiro numero"))
#
# if(num1<=num2 and num1<=num3):
#     if(num2<=num3):
#         print("A ordem e %0.2f %0.2f %0.2f" %(num1,num2,num3))
#     else:
#         print("A ordem e %0.2f %0.2f %0.2f" % (num1, num3, num2))
#
# elif(num2<=num1 and num2<=num3):
#     if(num1<=num3):
#         print("A ordem e %0.2f %0.2f %0.2f" %(num2,num1,num3))
#     else:
#         print("A ordem e %0.2f %0.2f %0.2f" % (num2, num3, num1))
# else:
#     if(num2<=num1):
#         print("A ordem e %0.2f %0.2f %0.2f" %(num3,num2,num1))
#     else:
#         print("A ordem e %0.2f %0.2f %0.2f" % (num3, num1, num2))


#15- Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.

# letra = input("Digite uma letra")
#
# if(letra in'aAeEiIoOuU'):
#     print("A letra digitada é vogal")
# else
#     print("A letra digitada não é uma vogal")


# 16) Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E.
#  Os endereços no intervalo de 0 à 127 são classe A,
#  de 128 a 191 são classe B,
#  de 192 a 223 são classe C,
# de 224 à 239 são classe D
#  e a partir de 240 são classe E.
# Faça um algoritmo que leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.

# num = int(input("Digite um numero"))
#
# if(num>=0 and num<= 127):
#     print("Pertence a classe A")
# elif(num>=128 and num<= 191):
#     print("Pertence a classe B")
# elif(num>=192 and num <= 223):
#     print("Pertence a classe C")
# elif (num >= 224 and num<= 239):
#     print("Pertence a classe D")
# elif(num>240):
#     print("Pertence a classe D")
# else:
#     print("Essa classe não existe")


# 17) Faça um algoritmo que receba um número inteiro,que represente um determinado mês do ano,
#  e mostre o nome do mês correspondente. Por exemplo, se for informado o número 2,
#  o algoritmo deverá exibir: fevereiro.O algoritmo também deve validar se a entrada está correta.


# num = int(input("Digite um numero"))
#
# if(num==1):
#     print("Mes Janeiro")
# elif(num==2):
#     print("Mes Fevereiro")
# elif(num==3):
#     print("Mes Março")
# elif(num==4):
#     print("Mes Abril")
# elif(num==5):
#     print("Mes Maio")
# elif(num==6):
#     print("Mes Junho")
# elif(num==7):
#     print("Mes Julho")
# elif(num==8):
#     print("Mes Agosto")
# elif (num == 9):
#     print("Mes Setembro")
# elif (num == 10):
#     print("Mes Outubro")
# elif (num == 11):
#     print("Mes Novembro")
# elif (num == 12):
#     print("Mes Dezembro")
# else:
#     print("Esse mes não existe")