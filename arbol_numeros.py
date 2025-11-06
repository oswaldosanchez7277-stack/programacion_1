from graphviz import Digraph
dot = Digraph(comment='arbol_simple')
dot.node('B', '1')
dot.node('A', 'Raiz')
dot.node('C', '3')
dot.node('D', '6')
dot.node('E', '8')
dot.node('F', '10')
dot.edges(['AB', 'AC'])
dot.edges(['AD', 'AE'])
dot.edges(['AF'])
dot.render('arbol_simple', view=True) # Esto debería funciona