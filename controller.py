from model import*
from random import randint
identificador = {}
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
                                if self.tarefa == "":
                                    print("Tarefa inválida")
                                else:
                                    if ToDO.AdicionarTarefa(self.tarefa, id, status):
                                        print("Tarefa adicionada")
                                        identificador[cont]=[self.tarefa]
                                        break
                                    else:
                                        print("Tarefa não adicionada")
                                        break
                else:
                    if self.tarefa == "":
                        print("Tarefa inválida")
                    else:
                        if ToDO.AdicionarTarefa(self.tarefa, id, status) == True:
                            print("Tarefa adicionada")
                        else:
                            print("Tarefa não adicionada")
            except Exception:
                print("Inválido")
            

class ControllerExcluirTarefa():
    def __init__(self,excluir):
        leave = 0
        while leave ==0:
            try:
                x = int (excluir)
                self.excluir = x-1
                if ToDO.ExcluirTarefa(self.excluir) == True:
                    print("Tarefa excluída")
                    leave  = 1
                else:
                    print("Algum problema foi encontrado")
                    
            except Exception:
                print("Valor inválido")
                excluir = input("Qual tarefa deseja excluir? ")

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
            
class ControllerAlterarTarefa():
    def __init__(self, taref, novatarefa):
        self.newtarefa = novatarefa
        self.tarefaId = taref
        for self.tarefaId in identificador:
            pass
    


class ControllerConcluirTarefa():
    def __init__(self):
        pass
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
            

