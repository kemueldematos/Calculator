def soma():
    print("")
    k = int(input("Insira o primeiro valor:"))
    s = int(input("Insira o segundo valor:"))
    
    sk = k + s
    print("O valor da soma é = ",sk)





while True:

    menu = """
        ========== CALCULADORA ==========

        Selecione a Operação desejada de acordo com seu número:

            1. Adicionar
            2. Subtrair
            3. Multplicar
            4. Dividir
            5. Encerrar o programa

        """

    print(menu)
    opcao = int(input())

    if opcao == 1:
        soma()
            
    elif opcao == 2:
        subtracao()
        
    elif opcao == 3:
        multiplicacao()
            
    elif opcao == 4:
        divisao()
            
    elif opcao == 5:
        print("")
        print("Programa Encerrado")
        break
        
    else:
        print("Opção Inválida, tente novamente:")
        print("")
        
