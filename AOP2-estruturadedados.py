class Nodo: #classe que representa o nó da lista
    def __init__(self, dado=0, proximoNodo=None):
        self.dado = dado
        self.proximo = proximoNodo
    
    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'
    
    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo
    
#>>Criar 10 clientes(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10)
#>>Inserir o cliente c1 10 vezes na lista, sendo cada vez com um valor diferente de conta( usar estes valores de conta: 1000,900,800,700,600,500,400,300,200,100)

#criar uma lista utilizando a classe cliente() para incluir os 10 clientes em nó em uma lista encadeada e cada nó possa armazenar o nome do cliente e uma lista de valores de conta

##Primeira parte incluindo os clientes na lista: 

class Cliente(): #classe que representa o cliente
    def __init__(self, nome, valorDaConta, nodo = None):
        self.nome = nome 
        self.valorDaConta = valorDaConta
        self.inicio = nodo
        self.tamanhoDaLista = 0

    def __repr__(self):
        return f'{self.nome} - {self.valorDaConta}'

    def adicionarClientesFinal(self, nomeCliente): #adiciona um novo cliente ao final da lista
        novoNodo = Nodo(nomeCliente)
        if self.inicio == None:
            self.inicio = novoNodo
        else:
            ultimoNodo = self.inicio
            while ultimoNodo.proximo:
                ultimoNodo = ultimoNodo.proximo
            ultimoNodo.proximo = novoNodo
        self.tamanhoDaLista += 1

    def mostrarListaClientes(self):
        mostrarNodos = ''
        nodoAtual = self.inicio
        while nodoAtual != None:
            mostrarNodos += f'{nodoAtual.dado} -> '
            nodoAtual = nodoAtual.proximo
        print(mostrarNodos)


listaClienteContas = Cliente("Lista de Clientes", [])
listaClienteContas.adicionarClientesFinal("c1")
listaClienteContas.adicionarClientesFinal("c2")

listaClienteContas.mostrarListaClientes()



#>>Percorrer a lista a fim de descobrir quantas ocorrências tem de cada cliente e assim  computar a média para cada cliente.  
#>>Inserir a média de conta computada de cada cliente, já ordenada em ordem crescente de valor em uma fila circular.
#>>Ler a Fila Circular e exibir a média de cada cliente, uma por linha. Imprimir somente os valores. 

