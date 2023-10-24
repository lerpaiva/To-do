from model import*
from random import randint

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
            try:
                self.tarefa = tarefa
                id = randint(1000,9999)
                cont=-1
                if len(ToDO.ListarTarefa()) > 1:
                    for tarefas in ToDO.ListarTarefa():
                        cont+=1
                        if cont >=1:
                            tarefas = tarefas[:4]
                            tarefas = int(tarefas)
                            if id != tarefas:
                                if self.tarefa == "":
                                    print("Tarefa inválida")
                                else:
                                    if ToDO.AdicionarTarefa(self.tarefa, id):
                                        print("Tarefa adicionada")
                                        break
                                    else:
                                        print("Tarefa não adicionada")
                                        break
                else:
                    if self.tarefa == "":
                        print("Tarefa inválida")
                    else:
                        if ToDO.AdicionarTarefa(self.tarefa, id) == True:
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

        controllerLista = ToDO.ListarTarefa()
        cont = -1
        for tarefas in controllerLista:
            cont+=1
            if cont>=1:
                tarefas = tarefas[7:-1]
                print(f"{cont} - {tarefas.strip()}")
            





