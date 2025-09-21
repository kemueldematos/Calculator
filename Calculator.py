# FAZER PORTENTAGEM
# IMPLEMETAR LISTAS E DICIONÁRIOS
# ATUALIZAR O README



def soma():
    print("")
    k = input("Insira o primeiro valor: ")
    s = input("Insira o segundo valor: ")
    
    try:
    
        k = float(k)
        s = float(s)
        sk = k + s
        print("O resultado da adicão é =", sk) 

    except ValueError:
        print("ERRO! OS DOIS VALORES À SEREM INSERIDOS DEVEM SER APENAS NÚMEROS")
    
def subtracao():
    print("")
    k = input("Insira o primeiro valor: ")
    s = input("Insira o segundo valor: ")
    
    try:
    
        k = float(k)
        s = float(s)
        sk = k - s
        print("O resultado da subtração é =", sk) 

    except ValueError:
        print("ERRO! OS DOIS VALORES À SEREM INSERIDOS DEVEM SER APENAS NÚMEROS") 
    
def multiplicacao():
    print("")
    k = input("Insira o primeiro valor: ")
    s = input("Insira o segundo valor: ")
    
    try:
    
        k = float(k)
        s = float(s)
        sk = k * s
        print("O resultado da multiplicação é =", sk) 

    except ValueError:
        print("ERRO! OS DOIS VALORES À SEREM INSERIDOS DEVEM SER APENAS NÚMEROS") 
        
def divisao():
    print("")
    k = input("Insira o primeiro valor: ")
    s = input("Insira o segundo valor: ")    
    
    try: 
        k = float(k)
        s = float(s)
        sk = k / s
        print("O resultado da Divisão é =", sk)
        
    except ValueError:
        print("ERRO! OS DOIS VALORES À SEREM INSERIDOS DEVEM SER APENAS NÚMEROS")
    
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
        print("Opção Inválida, tente novamente!")
        print("")
        
