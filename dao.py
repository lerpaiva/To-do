
arquivo = "To-Do.txt"
    
class DaoAdicionarTarefa:

    def adicionarTarefa(self, tarefa, x):
        with open(arquivo,"a") as arq:
            arq.write(f"{x} \t {tarefa}\n")
            return True
       
class DaoListarTarefa:
    def listarTarefa():
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()
        return linhas
            
            

