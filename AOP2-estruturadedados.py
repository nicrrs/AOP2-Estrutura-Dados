class Nodo: #classe que representa o nó da lista
    def __init__(self, dado=0, proximoNodo=None, valorDaConta=None):
        self.dado = dado
        self.proximo = proximoNodo
        self.valorDaConta = valorDaConta if valorDaConta is not None else []
    
    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'
    
    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo
    
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
                medias[atual.dado] = sum(atual.valorDaConta) / len(atual.valorDaConta) #calcula a média
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

class FilaCircular: #classe que representa a fila circular
    def __init__(self, media):
        self.inicio = None
        self.media = None
    
    def adicionarMedia(self, media): #adiciona a média na fila circular
        novoNodo = Nodo(media)
        if self.inicio is None:
            self.inicio = novoNodo
            novoNodo.proximo = novoNodo
        else:
            nodoTemporario = self.inicio
            while (nodoTemporario.proximo != self.inicio):
                nodoTemporario = nodoTemporario.proximo
            nodoTemporario.proximo = novoNodo
            novoNodo.proximo = self.inicio

    def mostrarFila(self): #exibir a fila circular
        if self.inicio is None:
            print(self.inicio.dado)
            return
        nodoTemporario = self.inicio
        while(True):
            print(nodoTemporario.dado)
            nodoTemporario = nodoTemporario.proximo
            if nodoTemporario == self.inicio:
                break

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
#print("Médias dos clientes:", medias)

filaCircular = FilaCircular(len(medias)) #cria a fila circular
for media in sorted(medias.values()): #adiciona a média na fila circular em ordem crescente
    filaCircular.adicionarMedia(media)

print("Média dos valores em ordem crescente:")
filaCircular.mostrarFila() #exibe a fila circular com as médias dos valores 
