menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)
    if opcao == "d":
        deposito = float(input("Informe o valor do deposito: " ))
    

    elif opcao == "s":
        saque = float(input("informe o valor do saque: "))



    elif opcao == "e":
        print (extrato)


    elif opcao == "q":  
        break
    else:
        print ("operacao invalida. por favor, selecione novamente a operacao desejada.")
