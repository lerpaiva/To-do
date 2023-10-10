arquivo = "To-Do.txt"

class DaoAdicionarTarefa:
    def adicionarTarefa(tarefa):
        with open(arquivo,"a") as arq:
            arq.write(f"{tarefa}\n")
        return True

class DaoListarTarefa:
    def listarTarefa():
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()
        return linhas
            
            

