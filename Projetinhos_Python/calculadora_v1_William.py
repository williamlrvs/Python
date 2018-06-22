# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
opcao = int(input("Digite sua opção (1/2/3/4): \n"))
if opcao > 4:
    print("Opção Inválida")
else:
    num_1 = int(input("\nDigite o primeiro número: "))
    num_2 = int(input("\nDigite o segundo número: "))

    if opcao == 1:
        soma = lambda a, b: a + b
        print("\n{} + {} = {}".format(num_1, num_2, soma(num_1, num_2)))
    elif opcao == 2:
        subtracao = lambda a, b: a - b
        print("\n{} - {} = {}".format(num_1, num_2, subtracao(num_1, num_2)))
    elif opcao == 3:
        multiplica = lambda a, b: a * b
        print("\n{} * {} = {}".format(num_1, num_2, multiplica(num_1, num_2)))
    elif opcao == 4:
        divisao = lambda a, b: a / b
        print("\n{} / {} = {}".format(num_1, num_2, divisao(num_1, num_2)))
    else:
        print("Opção inválida...")
