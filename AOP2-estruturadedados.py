class Nodo: #classe que representa o nó da lista
    def __init__(self, dado=0, proximoNodo=None, valorDaConta=None):
        self.dado = dado
        self.proximo = proximoNodo
        self.valorDaConta = valorDaConta if valorDaConta is not None else []
    
    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'
    
    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo
    
#Primeira parte incluindo os clientes na lista: 

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
    
    def adicionarValor(self, nome, valorDaConta):
        atual = self.inicio
        while atual is not None:
            if atual.dado == nome:
                atual.valorDaConta.append(valorDaConta)
                break
            atual = atual.proximo

    def mostrarListaClientes(self): #exibir a lista de clientes
        mostrarNodos = ''
        nodoAtual = self.inicio
        while nodoAtual != None:
            mostrarNodos += f'{nodoAtual.dado} -> '
            nodoAtual = nodoAtual.proximo
        print(mostrarNodos)


listaClienteContas = Cliente("Lista de Clientes", [])

for i in range(1, 11): #adicionando os clientes na lista
    listaClienteContas.adicionarClientesFinal(f"c{i}")


listaClienteContas.mostrarListaClientes()



#>>Percorrer a lista a fim de descobrir quantas ocorrências tem de cada cliente e assim  computar a média para cada cliente.  
#>>Inserir a média de conta computada de cada cliente, já ordenada em ordem crescente de valor em uma fila circular.
#>>Ler a Fila Circular e exibir a média de cada cliente, uma por linha. Imprimir somente os valores.

