def create():
    print("\n********************************")
    print("**** CADASTRO DE NOVO ALUNO ****")
    print("********************************\n")

    id = "1;"
    nome = input("informe o nome do aluno: ") + ";"
    matricula = input("informe a matrícula do aluno: ") + ";"
    idade = input("informe a idade do aluno: ") + ";"
    nota = input("informe a nota do aluno: ") + "\n"

    file = open("banco_de_dados.csv", "r+")

    line = file.readlines()[-1]
    aluno = line.split(";")

    if (aluno[0] != "id"):
        id = str(int(aluno[0]) + 1) + ";"

    file.writelines([id, nome, matricula, idade, nota])

    file.close()

def read():

    print("\n********************************")
    print("****** LISTAGEM DE ALUNOS ******")
    print("********************************\n")
    file = open("banco_de_dados.csv", "r")

    lines = file.readlines()

    for i in range(2,len(lines)):
        line = lines[i].split(";")
        print("id: ", line[0])
        print("nome: ", line[1])
        print("matricula: ", line[2])
        print("idade: ", line[3])
        print("nota: ", line[4])
        print("================================")

    file.close()

def update(id):
    print("\n********************************")
    print("***** EDITAR DADOS DO ALUNO ****")
    print("********************************\n")
    file = open("banco_de_dados.csv", "r")

    lines = file.readlines()

    aluno_exists = False

    for i in range(2,len(lines)):
        line = lines[i].split(";")
        if str(id) == line[0]:
            aluno_exists = True

            id = line[0] + ";"
            nome = input("informe o nome do aluno: ") + ";"
            matricula = input("informe a matrícula do aluno: ") + ";"
            idade = input("informe a idade do aluno: ") + ";"
            nota = input("informe a nota do aluno: ") + "\n"

            lines[i] = id + nome + matricula + idade + nota
            break
    
    file.close()

    if aluno_exists:
        file = open("banco_de_dados.csv", "w")

        file.writelines(lines)
        if lines[-1][-1] != "\n":
            file.write("\n")

        file.close()
    else:
        print("aluno não existe")
        input("pressione qualquer tecla para continuar")

def delete(id):
    print("\n********************************")
    print("** DELETAR CADASTRO DE ALUNO ***")
    print("********************************\n")
    file = open("banco_de_dados.csv", "r")

    lines = file.readlines()

    aluno_exists = False

    for i in range(2,len(lines)):
        line = lines[i].split(";")
        if str(id) == line[0]:
            aluno_exists = True

            lines.pop(i)
            break
    
    file.close()

    if aluno_exists:
        file = open("banco_de_dados.csv", "w")

        file.writelines(lines)

        file.close()
    else:
        print("aluno não existe")
        input("pressione qualquer tecla para continuar")