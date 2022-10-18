from menu import menu
import crud

while True:
    opcao = menu()

    if opcao == 1:
        crud.read()
        input("pressione qualquer tecla para continuar")
    elif opcao == 2:
        print("em desenvolvimento...")
        input("pressione qualquer tecla para continuar")
    elif opcao == 3:
        crud.create()
    elif opcao == 4:
        id = input("informe o id do aluno a ser editado: ")
        crud.update(id)
    elif opcao == 5:
        id = input("informe o id do aluno a ser excluido: ")
        crud.delete(id)
    elif opcao == 6:
        print("em desenvolvimento...")
        input("pressione qualquer tecla para continuar")
    else:
        break