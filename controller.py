from model import*
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
                                if self.tarefa == "":
                                    print("Tarefa inválida")
                                else:
                                    if ToDO.AdicionarTarefa(self.tarefa, id, status):
                                        print("Tarefa adicionada")
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
    def __init__(self, indice, novatarefa):
        try:
            if novatarefa =="":
                print("Inválido")
            else:
                Lista_id = []
                cont = 0
                for linha in ToDO.ListarTarefa():
                    cont +=1 
                    linha = linha('|', 3)
                    letra = linha[0]
                    if letra == "A":
                        id = lista[1]
                        id = int(id)
                        Lista_id.append(id)
                    
                for linha in ToDO.ListarTarefa():
                    lista = linha.split('|', 3)
                    tarefa_A = lista[2]
                    id = lista[1]
                    id = int(id)
                    if id == Lista_id[indice]:
                        ToDO.AlterarTarefa(tarefa_A, novatarefa)
                        break

        except Exception:
            print("Inválido")




        

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
                        return "Inválido"
                else:
                    return "Inválido"
            

