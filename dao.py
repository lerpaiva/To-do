from random import randint
arquivo = "To-Do.txt"
ids = []

    
class DaoAdicionarTarefa:
    def adicionarTarefa(self, tarefa):
        self.id = randint(1000, 9999)
        ids.append(self.id)
        with open(arquivo,"a") as arq:
            id = randint(1000, 9999)
            if id in ids:
                return False
            else:
                arq.write(f"{id} \t {tarefa}\n")
                return True
       
class DaoListarTarefa:
    def listarTarefa():
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()
        return linhas
            
            

