def menu():
    opcao = -1
    while opcao < 0 or opcao > 6:
        print("escolha uma operação:")
        print("1- visualizar alunos")
        print("2- visualizar aluno em específico")
        print("3- adicionar novo aluno")
        print("4- editar aluno já existente")
        print("5- excluir aluno")
        print("6- mostrar media das notas")
        print("0- sair")

        opcao = int(input("opção: "))

    return opcao