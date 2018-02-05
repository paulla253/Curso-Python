#-------------------------------------------------------
#Nome : Ana Paula Fernandes de Souza
#Atualização : 05/02/2018
#Lista 1
#Assunto : Conceitos da Programação e do Python
#-------------------------------------------------------


#1-Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.

# print("Ana Paula")

#2-Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase
# para a saída padrão: "O seu nome é: [nome do usuário]".

# nome = input("Digite seu nome: ")
# print("Seu nome é ", nome)

#3-Faça um algoritmo que solicite o nome e a idade do usuário e então,
#  envie a seguinte frase para o Console: "O seu nome é <nome> e a sua idade é <idade>".

# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade : ")
# print("Seu nome é "+nome+" e sua idade é "+idade)

#4-Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa variável
# e por fim, envie esse número para a saída padrão.

#5-Faça um algoritmo que solicite ao usuário informar um número. Em seguida,
# escreva a seguinte mensagem: "O número digitado foi: ".

# num=input("Digite um numero:")
# print("O numero é ", num)

#6-Faça um algoritmo que solicite ao usuário informar 3 números. Em seguida,
#  some-os e envie para a saída padrão a seguinte frase: "A soma total é:

# num1=input("Digite o 1º numero:")
# num2=input("Digite o 2º numero:")
# num3=input("Digite o 3º numero:")
#
# soma=int(num1)+int(num2)+int(num3)
#
# print("A soma é  ", soma)

#7-Faça um algoritmo que solicite ao usuário informar 2 números. Em seguida, some os valores
# e envie para a saída padrão a seguinte frase: "A soma entre <X> e <Y> é igual <total>".

# num1=input("Digite o 1º numero:")
# num2=input("Digite o 2º numero:")
#
# soma=int(num1)+int(num2)
#
# print("A soma de "+num1+" + "+num2+" eh ", soma)


#8-Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário.
# Em seguida, calcule e envie para a saída padrão a média:


# num1=input("Digite o 1º numero:")
# num2=input("Digite o 2º numero:")
# num3=input("Digite o 3º numero:")
# num4=input("Digite o 4º numero:")
#
# media=(int(num1)+int(num2)+int(num3)+int(num4))/4
#
#
# print("A media é  ", media)


#9-Faça um algoritmo em que o usuário informe uma medida em metros.
# Em seguida, converta essa medida para centímetros e envie para a saída padrão:

# metros=input("Digite um números em metros :")
#
# print("O número em metros "+metros+ "convertido para centimentros é ", int(metros)*100)

#10-Faça um algoritmo que calcule o cubo e o quadrado de um determinado número:

# num1=input("Digite um numero:")
#
# print("O quadrado do número é ", int(num1)**2)
# print("O cubo do número é ", int(num1)**3)


# 11- Faça um algoritmo que solicite ao usuário digitar 2 números.
# Em seguida, imprima o total decimal da divisão e o total inteiro (sem casas decimais):

# num1=float(input("Digite o 1º numero:"))
# num2=float(input("Digite o 2º numero:"))
#
# divisao = num1 / num2
#
#
# print("Resultado decimal: %.2f" % (divisao))
# print("Resultado inteiro: %i" % (divisao))



# 12- Faça um algoritmo que solicite a largura e a altura de um quadrado.
# Em seguida, imprima para o usuário quantos metros quadrados possui a área total do quadrado.

# largura=input("Digite a largura:")
# altura=input("Digite a altura:")
#
# print("A área total do quadrado em metros é ", int(largura)*int(altura))

#13- Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas, minutos e segundos.
#  Em seguida, converta tudo para segundos:


# dias=input("Digite a quantidade de dias:")
# horas=input("Digite a quantidade de horas:")
# minutos=input("Digite os minutos:")
# seguntos=input("Digite os segundos:")
#
#
# print("O total em segundos é  ", (int(dias)*24*60*60*60)+(int(horas)*60*60)+(int(minutos)*60)+int(seguntos))

#14- Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida, aplique 10% de desconto e
#  imprima na tela tanto o valor total como também o valor com o desconto aplicado.


# valor=float(input("Digite o valor da compra : "))
#
# compra=valor*0.9;
#
# print("Valor a pagar ",compra)
# print("Desconto de %.2f" %(valor - compra))
