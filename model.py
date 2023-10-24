from dao import*
class ToDo():


    def AdicionarTarefa(self, tarefa, x):
        add = DaoAdicionarTarefa()
        return add.adicionarTarefa(tarefa, x)

    #def ExcluirTarefa(self, excluir):
     #   self.lista.pop(excluir)
     #   return True

    def ListarTarefa(self):
        return DaoListarTarefa.listarTarefa()
    


ToDO = ToDo()
