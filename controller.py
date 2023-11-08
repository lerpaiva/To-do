from model import *
from random import randint

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
            try:
                self.tarefa = tarefa
                id = randint(1000,9999)
                status = "A"
                cont=-1
                if len(ToDO.ListarTarefa()) > 1:
                    for tarefas in ToDO.ListarTarefa():
                        cont+=1
                        if cont >=1:
                            tarefas = tarefas.split('|', maxsplit=3)
                            tarf =tarefas[1]
                            tarf = int(tarf)
                            if id != tarefas:
                                if self.tarefa == "" or self.tarefa==" ":
                                    print("Tarefa inválida")
                                else:
                                    if ToDO.AdicionarTarefa(self.tarefa, id, status):
                                        print("Tarefa adicionada")
                                        break
                                    else:
                                        print("Tarefa não adicionada")
                                        break
                else:
                    if self.tarefa == "" or self.tarefa == " ":
                        print("Tarefa inválida")
                    else:
                        if ToDO.AdicionarTarefa(self.tarefa, id, status) == True:
                            print("Tarefa adicionada")
                        else:
                            print("Tarefa não adicionada")
            except Exception:
                print("Inválido")
            

class ControllerListarTarefa():
    def __init__(self):
        cont= -1
        if len(ToDO.ListarTarefa())>1:
            for tarefas in ToDO.ListarTarefa():
                tarefax = tarefas.split('|', maxsplit=3)
                cont += 1
                if cont >= 1:
                    tarefaz = tarefax[0]
                    tarefarr = tarefax[2]
                    tarefarr = tarefarr[1:]
                    if "A" in tarefaz:
                        print(f"{cont} - {tarefarr}")
                    else:
                        cont-=1
                    
class ControllerAlterarTarefa():
    def __init__(self, indice, novatarefa):
        indice = int(indice)
        try:
            if novatarefa =="" or novatarefa == " " or indice <=0 :
                print("Inválido")
            else:
                cont=0
                Lista_id = []
                for linha in ToDO.ListarTarefa():
                    cont+=1
                    if cont > 0:

                        letra = linha[0]
                        if letra == "A":
                            linhar = linha.split('|', 3)
                            id = linhar[1]
                            id = int(id)
                            Lista_id.append(id)

                if indice <= len(Lista_id):
                    indice -=1
                    cont = -1
                    for linha in ToDO.ListarTarefa():
                        cont+=1
                        if cont > 0:
                            linhar = linha.split('|', 3)
                            id = linhar[1]
                            id = int(id)
                            letrinha = linhar[0]

                            if id == Lista_id[indice]:
                                if "A" in letrinha:
                                    novatarf = (f"{letrinha}|\t{id} |\t{novatarefa}\n")
                                    alterando = ToDO.AlterarTarefa(linha, novatarf)
                                    if alterando == True:
                                        print("Tarefa alterada com sucesso!")
                                        break
                                    else:
                                        print("Alteração inválida")
                                else: 
                                    break



        except Exception as erro:
            print(erro)

class ControllerConcluirExcluirTarefas():
    def __init__(self, indice,newStats):
        indice = int(indice)
        try:
            if newStats =="" or newStats == " "or indice <=0 :
                print("Inválido")
            else:
                cont=0
                Lista_id = []
                for linha in ToDO.ListarTarefa():
                    cont+=1
                    if cont > 0:

                        letra = linha[0]
                        if letra == "A":
                            linhar = linha.split('|', 3)
                            id = linhar[1]
                            id = int(id)
                            Lista_id.append(id)

                if indice <= len(Lista_id):
                    indice -=1
                    cont = -1
                    for linha in ToDO.ListarTarefa():
                        cont+=1
                        if cont > 0:
                            linhar = linha.split('|', 3)
                            id = linhar[1]
                            id = int(id)
                            tarefinha = linhar[2]
                            letrinha = linhar[0]

                            if id == Lista_id[indice]:
                                if "A " in letrinha:
                                    novatarf = (f"{newStats} |\t{id} |{tarefinha}")
                                    alterando = ToDO.AlterarTarefa(linha, novatarf)
                                    if alterando == True:
                                        print("Tarefa alterada com sucesso!")
                                        break
                                    else:
                                        print("Alteração inválida")
                                else: 
                                    break



        except Exception as erro:
            print(erro)


        

class ControllerTarefasConcluidas():
    def __init__(self):
        cont= -1
        if len(ToDO.ListarTarefa())>1:
            for tarefas in ToDO.ListarTarefa():
                tarefax = tarefas.split('|', maxsplit=3)
                cont += 1
                if cont >= 1:
                    tarefaz = tarefax[0]
                    tarefarr = tarefax[2]
                    tarefarr = tarefarr[1:]
                    if "C" in tarefaz:
                        print(f"{cont} - {tarefarr}")
                    else:
                        cont -=1

            

