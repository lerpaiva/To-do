from dao import*
class ToDo():


    def AdicionarTarefa(self, tarefa):
        add = DaoAdicionarTarefa()
        return add.adicionarTarefa(tarefa)

    #def ExcluirTarefa(self, excluir):
     #   self.lista.pop(excluir)
     #   return True

    def ListarTarefa(self):
        listar = DaoListarTarefa()
        return listar.listarTarefa()
    


ToDO = ToDo()
