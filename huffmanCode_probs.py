
class Node: # declaracion de variables para crear los nodos
    # properties
    
    symbol = ""
    encoding = "" 
    visited = False
    parent = -1 # longitud de 0 a -1

class Huffman: # declaracion de variables para la creacion del arbol de Huffman
    Tree = None # retornar arbol
    Root = None # retornar raiz
    Nodes = [] #Lista
    probs = {} #diccionario
    dictEncoder = {}
    
    # methods
    def __init__(self, symbols): #en este metodo inicializamos las funciones con los atributos que vamos a utilizar
        self.initNodes(symbols)
        self.buildTree()
        self.buildDictionary()

    def initNodes(self, probs): # creamos los nodos con sus respectivas probabiliddes
        for symbol in probs:
            print("probs_", probs)
            print("symbol_", symbol)
            node = Node() # inicializamos el node
            node.symbol = symbol # lee la llave del diccionario
            node.probability = probs[symbol] # asignamos una probabilidad a cada simbolo o letra. Lee la probabilidad de acuerdo al simbolo en el diccionario
            print("node.probability_", node.probability )
            node.visited = False # variable q no es fija que va ir cambiando 
            self.Nodes.append(node) # creamos una lista por cada nodo creado
            self.probs[symbol]=probs[symbol]  # establece para cada probabilidad un simbolo         


    def buildTree(self): # Realizamos las operaciones de acuerdo al reglamento para la construccion del arbol de Huffman
        indexMin1 = self.getNodeWithMinimumProb() # Buscamos el menor numero de la primera probabilidad
        indexMin2 = self.getNodeWithMinimumProb() # Buscamos el menor numero de la segunda probabilidad 
        
        while indexMin1 != -1 and indexMin2 != -1: # != evalúa como verdadero si 2 variables son diferentes
            node = Node() # inicializamos
            #node.symbol = "."
            #print("Node.symbol", node.symbol)
            node.encoding = ""
            # llamamos a las dos probabilidades minimas
            prob1 = self.Nodes[indexMin1].probability
            prob2 = self.Nodes[indexMin2].probability
            node.probability = prob1 + prob2 # sumamos las probabilidades
            node.visited = False # false = 1
            node.parent = -1 # restamos la probabilidad a -1
            self.Nodes.append(node)
            self.Nodes[indexMin1].parent = len(self.Nodes) - 1 #  lista o cadena que queremos medir
            self.Nodes[indexMin2].parent = len(self.Nodes) - 1
            
            # Regla: 0 a mayor probabilidad, 1 a menor probabilidad.
            if prob1 >= prob2:
                self.Nodes[indexMin1].encoding = "0"
                self.Nodes[indexMin2].encoding = "1"
            else:
                self.Nodes[indexMin1].encoding = "1"
                self.Nodes[indexMin2].encoding = "0"
            
            indexMin1 = self.getNodeWithMinimumProb()
            indexMin2 = self.getNodeWithMinimumProb()
            print("indexMin1_",indexMin1)
            print("indexMin2_",indexMin2)
    def getNodeWithMinimumProb(self): # realizamos una comparacion para obtener el nodo de menor probabilidad
        minProb = 1.0   # La minima probabilidad no puede ser mayor de 1
        indexMin = -1 # indice para restar a la probalidad

        for index in range(0, len(self.Nodes)): # index es el numero de probabilidad este for recorre los nodos y guarda la menor probabilidad y su indice cada vez
            if (self.Nodes[index].probability < minProb  and 
               (not self.Nodes[index].visited)):
                minProb = self.Nodes[index].probability
                indexMin = index
                print("index_self_nodes: ", index)

        if indexMin != -1: #se detiene cuando el indice es -1, el true significa que ya pasó por ese nodo
            self.Nodes[indexMin].visited = True
            print("indexMin",indexMin)

        return indexMin
   
    def showSymbolEncoding(self, symbol): # designamos un codigo binario a cada simbolo resuelto por el arbol de Huffman
        found = False
        index = 0
        encoding = ""

        for i  in range(0, len(self.Nodes)):
            if self.Nodes[i].symbol == symbol:
                found = True
                index = i
                break 
        
        if found: # encontro 
            while index != -1: # si son diferentes
                encoding = "%s%s" % (self.Nodes[index].encoding, encoding)      
                index = self.Nodes[index].parent
      

        return encoding

    def buildDictionary(self): # creamos un diccionario, guardamos todos los simbolos con sus respectivos codigos binarios
                               # resueltos por el arbol de Huffman
        for symbol in self.probs:
            encoding = self.showSymbolEncoding(symbol)
            self.dictEncoder[symbol] = encoding
                
    def encode(self, plain): # agrupa los codigos binarios codificados de acuerdo al mensaje escrito en consola
        encoded = ""
        for symbol in plain:
            encoded = "%s%s" % (encoded, self.dictEncoder[symbol])

        return encoded

    # DECODIFICACION 
    def decode(self, encoded): # recibe la cadena del codigo binario enviado desde el emisor para decodificar
        index = 0
        decoded = ""
    

        while index < len(encoded): # mientras buscamos en la longitud de la parte codificada

    
            founf = False # establecemos una variable
    
            aux = encoded[index:] # va a buscar a cada parte codificada un simbolo
                                  # no va ser fija va ir buscando cual es compatible con cada una

    
            for symbol in self.probs:
                if aux.startswith(self.dictEncoder[symbol]): # se comprueba si la cadena es verdadera o falsa. si la parte axuliar inicia dentro del diccionario encodificado  nos va a dar
                    decoded = "%s%s" % (decoded, symbol) # parte decodificada
                    index = index + len(self.dictEncoder[symbol]) # busqueda para cada simbolo a cada probabilidad
                    break 
        
        return decoded

    #FIN DE LA DECODIFICACION

    




if __name__=="__main__":
    

    mensaje = input("\nDigit a word to compress: ")
    simbolos=''
    probabilidad=[]
    msm=mensaje
    d=0
    prob = {'a':'0.0575','b':'0.0128','c':'0.0263','d':'0.0285','e':'0.0913','f':'0.0173','g':'0.0133','h':'0.0313','i':'0.0599','j':'0.0006','k':'0.0084','l':'0.0335','m':'0.0235','n':'0.0596','o':'0.0689','p':'0.0192','q':'0.0008','r':'0.0508','s':'0.0567','t':'0.0706','u':'0.0334','v':'0.0069','w':'0.0119','x':'0.0073','y':'0.0164','z':'0.0007','-':'0.1928'}


    for i in mensaje:
        if i in msm:
            print (i,"=",int ( msm.count(i)))
            simbolos+=i
            probabilidad.append(float(prob.get(i)))
            msm=msm.replace(i,'')
            d+= 1
         
    symbols=dict(zip(simbolos, probabilidad))


    print ("number of compressed symbols=",d)
    print ("The probability of each symbol according with the table is: \n")
    print (symbols)
    #print LA FUNCION [buildTree] DEL CODIGO. ORDENA LAS PROBABILIDADES DE MENOR A MAYOR PROBABILIDAD
    #           Y REALIZA LAS OPERACIONES YA EXPLICADAS QUE SE REQUIEREN PARA IR ARMANDO EL ARBOL DE HUFFMAN
    

    
   

    # codificar instancia
    huffman = Huffman(symbols)
    print ("The codification for each symbol is: ")
    #5 PASO:CODIFICACION BINARIA USANDO EL ARBOL DE HUFFMAN
    
    for symbol in symbols:
        print ("Simbolo: %s; Codificacion: %s" % (symbol, huffman.showSymbolEncoding(symbol)))

    encoded = huffman.encode(mensaje)
    print ("The bit codification is : %s" % (encoded))
    print ("The length of your binary code is:  %s" % (len(encoded)))
    
    data = encoded
   
       # DECODIFICACION
  
    print ("Decodification")
    
    decoded = huffman.decode(data)
    print ("The code that you whant to decodify is :", data) 
    
    print ("Decodified message is:  " , (decoded))

   



    
