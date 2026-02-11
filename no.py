

class No:
    
    #Classe que representa um nó da árvore AVL.
  
    def __init__(self, info: str, linha: int):

        self.info: str = info          # Palavra armazenada no nó
        self.linhas: list = [linha]    # Lista de linhas em que a palavra aparece
        self.altura = 1                # Altura inicial do nó
        self.esq = None                # Ponteiro Filho esquerdo
        self.dir = None                # Ponteiro Filho direito

    def frequencia(self):
        
        #Retorna o número de linhas em que a palavra aparece.
        
        return len(self.linhas)







