from dao import*
class ToDo():


    def AdicionarTarefa(self, tarefa):
        DaoAdicionarTarefa.adicionarTarefa(tarefa)
        return True

    #def ExcluirTarefa(self, excluir):
     #   self.lista.pop(excluir)
     #   return True

    def ListarTarefa(self):
        return DaoListarTarefa.listarTarefa()
    


ToDO = ToDo()
