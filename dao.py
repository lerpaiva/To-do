
arquivo = "To-Do.txt"
    
class DaoAdicionarTarefa:

    def adicionarTarefa(self, tarefa, x, stat):
        with open(arquivo,"a") as arq:
            arq.write(f"\t{stat} |\t{x} |\t{tarefa}\n")
            return True
       
class DaoListarTarefa:
    def listarTarefa():
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()
        return linhas
            
class DaoAlterarTarefa:
    def alterarTarefa(self, novaTarefa):
        self.novaTarefa = novaTarefa
        with open(arquivo,"w") as arq:
            arq.write(f"{novaTarefa}")
            return True
                    

