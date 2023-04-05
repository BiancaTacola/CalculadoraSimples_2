'''a utilização de funções e parâmetros permite que o código seja mais modular e organizado, tornando mais fácil a
leitura, manutenção e reutilização de trechos de código.'''

def somar(a,b):
    # Essa função soma dois valores
    soma = a + b
    print("A soma é:", soma)

def subtrair(a,b):
    # Essa função subtrai dois valores
    subtracao = a - b
    print("A subtração é:", subtracao)

def multiplicar(a,b):
    # Essa função multiplica dois valores
    multiplicacao = a * b
    print("A multiplicação é:", multiplicacao)

def dividir(a,b):
    # Essa função divide dois valores
    if b != 0:
        divisao = a / b
        print("A divisão é:", divisao)
    else:
        print("Não é possível dividir por zero.")

# Código fora das funções
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

somar(valor1, valor2)
subtrair(valor1, valor2)
multiplicar(valor1, valor2)
dividir(valor1, valor2)
