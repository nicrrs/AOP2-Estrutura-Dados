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
    
    def adicionarValor(self, nome, valorDaConta): #adiciona o valor da conta do cliente
        atual = self.inicio
        while atual is not None:
            if atual.dado == nome:
                atual.valorDaConta.append(valorDaConta)
                break
            atual = atual.proximo
    
    def calculaMedia(self): #calcula a média dos valores da conta de cada cliente
        medias = {}
        atual = self.inicio
        while atual is not None:
            if atual.valorDaConta:
                medias[atual.dado] = sum(atual.valorDaConta) / len(atual.valorDaConta)
            else:
                medias[atual.dado] = 0
            atual = atual.proximo
        return medias

    def mostrarListaClientes(self): #exibir a lista de clientes
        mostrarNodos = ''
        nodoAtual = self.inicio
        while nodoAtual != None:
            mostrarNodos += f'{nodoAtual.dado} (Valores: {nodoAtual.valorDaConta}) -> '
            nodoAtual = nodoAtual.proximo
        print(mostrarNodos)


listaClienteContas = Cliente("Lista de Clientes", []) #cria a lista de clientes

for i in range(1, 11): #adiciona os clientes na lista
    listaClienteContas.adicionarClientesFinal(f"c{i}")

valores = {
    "c1": [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],
    "c2": [1000, 900, 800, 700, 600, 500, 400, 300, 200],
    "c3": [1000, 900, 800, 700, 600, 500, 400, 300],
    "c4": [1000, 900, 800, 700, 600, 500, 400],
    "c5": [1000, 900, 800, 700, 600, 500],
    "c6": [1000, 900, 800, 700, 600],
    "c7": [1000, 900, 800, 700],
    "c8": [1000, 900, 800],
    "c9": [1000, 900],
    "c10":[1000]
}

for cliente, valoresConta in valores.items(): #adicionando os valores na lista de clientes
    for valor in valoresConta:
        listaClienteContas.adicionarValor(cliente, valor)

#listaClienteContas.mostrarListaClientes() #para exibir a lista de clientes

medias = listaClienteContas.calculaMedia() #calcula e exibe a média dos valores
print("Médias dos clientes:", medias)



#>>Percorrer a lista a fim de descobrir quantas ocorrências tem de cada cliente e assim  computar a média para cada cliente.  
#>>Inserir a média de conta computada de cada cliente, já ordenada em ordem crescente de valor em uma fila circular.
#>>Ler a Fila Circular e exibir a média de cada cliente, uma por linha. Imprimir somente os valores.

