from model import*

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        leave = 0
        while leave == 0:
            try:
                self.tarefa = tarefa
                if self.tarefa  == "":
                    print("Informe uma tarefa válida")
                    leave = 1
                else:
                    if ToDO.AdicionarTarefa(self.tarefa) == True:
                            print("Tarefa adicionada")
                            leave =1
                    else:
                        print("Algum problema foi encontrado")
                        leave = 1
            except Exception:
                    print("Valor inválido")
                    leave =1
            

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
        cont = 1
        for tarefas in controllerLista:
            print(f"{cont} - {tarefas.strip()}")
            cont+=1





