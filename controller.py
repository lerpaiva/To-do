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
        try:
            if novatarefa =="" or novatarefa == " ":
                print("Inválido")
            else:
                cont=0
                Lista_id = []
                for linha in ToDO.ListarTarefa():
                    cont+=1
                    if cont > 0:

                        linhar = linha('|', 3)
                        letra = linhar[0]
                        if letra == "\tA":
                            id = lista[1]
                            id = int(id)
                            Lista_id.append(id)
                    
                for linha in ToDO.ListarTarefa():
                    lista = linha.split('|', 3)
                    tarefa_A = lista[2]
                    id = lista[1]
                    letrinha = lista[0]
                    id = int(id)
                    if id == Lista_id[indice]:
                        if letrinha == "\tA":
                            novatarf = (f"\t{letrinha} |\t{id} |\t{novatarefa}\n")
                            alterando = ToDO.AlterarTarefa(tarefa_A, novatarf)
                            if alterando == True:
                                print("Tarefa alterada com sucesso!")
                                break
                            else:
                                print("Alteração inválida")
                        else: 
                            break
                    else:
                        print("Inválido")



        except Exception as erro:
            print(erro)

class ControllerConcluirTarefas():
    def __init__(self, indice,newStats):
        try:
            if newStats =="" or newStats == " ":
                print("Inválido")
            else:
                cont=0
                Lista_id = []
                for linha in ToDO.ListarTarefa():
                    cont+=1
                    if cont > 0:

                        linha = linha('|', 3)
                        letra = linha[0]
                        if letra == "\tA":
                            id = lista[1]
                            id = int(id)
                            Lista_id.append(id)
                    
                for linha in ToDO.ListarTarefa():
                    lista = linha.split('|', 3)
                    tarefa_A = lista[2]
                    id = lista[1]
                    letrinha = lista[0]
                    id = int(id)
                    if id == Lista_id[indice]:
                        if letrinha == "\tA":
                            novatarf = (f"\t{newStats} |\t{id} |\t{tarefa_A}\n")
                            alterando = ToDO.AlterarTarefa(letrinha, novatarf)
                            if alterando == True:
                                print("Tarefa alterada com sucesso!")
                                break
                            else:
                                print("Alteração inválida")
                        else: 
                            break
                    else:
                        print("Inválido")



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

            

