'''
aluno:Pedro Henrique Rodrigues De souza.
s.i- manhã.
2025.1
01-Conceitos Básicos de Programação.
'''

first=float(input("Digite um numero: "))
second=float(input('digite outro numero: '))
# soma, subtração, multiplicação, divisão e resto da divisão.
soma= first+second 
subtraçao= first-second
multiplicaçao= first*second
divisao= first/second
resto_da_divisao= first % second
print("O Resultado da soma foi {}, da subtraçao {},o valor da multiplicaçao {}, o valor da divisao {}, e o resto da divisao é {}".format(soma,subtraçao,multiplicaçao,divisao,resto_da_divisao))

#2 Realiza a leitura de 1 inte imprime o seu antecessor e o seu sucessor.
number=int(input("Digite um numero inteiro."))
after= number+1
before=number-1
print("o seu antecessor é,",after,"e o seu sucessor é,", before)
