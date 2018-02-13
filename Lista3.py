#-------------------------------------------------------
#Nome : Ana Paula Fernandes de Souza
#Atualização : 05/02/2018
#Lista 3
#Assunto :  Iteradores
#-------------------------------------------------------


# 1-Faça um algoritmo que imprima os números no intervalo entre 1 e 100:

# x=1
#
# while(x<=100):
#     print(x)
#     x+=1;

#02- Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido
# para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso:


# inter=int(input("Digite um intervalo : "))
#
# x=1;
#
# while(x<=100):
#     print(x)
#     x+=inter

#03- Faça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:

# x=10;
#
# while(x>0):
#     print(x)
#     x-=1

#04- Faça um algoritmo que imprima os números pares entre 0 e 100:

# x=0
#
# while(x<=100):
#     print(x)
#     x+=2

#05- Faça um algoritmo que some a quantidade de números pares encontrados no intervalo entre 0 e 100:

# x=0
#
# qtd=0
#
# while(x<=100):
#     print(x)
#     x+=2
#     qtd+=1
# print("Quantidade de numeros par é ",qtd)

# 8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e
# permita que o mesmo possa definir 3 números que deverão ser ignorados,
# ou seja, que não serão impressos na tela:

# inicio=int(input("Digite um numero para comecar o loop : "))
# fim=int(input("Digite um numero para finalizar o loop :"))
# passo=int(input("Digite um numero para ser o passo do loop :"))
#
# num1=int(input("Primeiro numero para ser ignorado : "))
# num2=int(input("Segundo numero para ser ignorado : "))
# num3=int(input("Terceiro numero para ser ignorado : "))
#
# x=0
#
# while(x<=fim):
#     if(x!=num1 and x!=num2 and x!=num3):
#         print(x)
#     x+=passo

# 9) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida,
#  solicite ao usuário digitar uma letra. Caso a letra seja o "q" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:

# letra ='a'
# while(letra!='q'):
#
#     letra=input("Estou em looping,Digite uma letra")