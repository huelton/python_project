# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
from constantes import TIPO_FILA_PRIORITARIA, TIPO_FILA_NORMAL

# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(3))
# print(fila_teste.chamacliente(1))
# print(fila_teste.chamacliente(2))

# fila_teste2 = FilaNormal()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
#
# print(fila_teste2.chama_cliente(2))
# print(fila_teste2.chama_cliente(1))
#print(fila_teste2.estatistica('10/04/2020', 6400, 'detail'))

# Nesta aula necessario precisa criar o repositorio no GITHUB para poder instalar:
#  flake8 --install-hook git
# Encontra o repositorio e instalar o projeto para poder ser gerenciado pelo Flake8 depois
# config --bool flake8.strict true esse comando evita commit com problemas de arquivo não parametrizados no arquivo tox.ini


teste_fabrica = FabricaFila.pega_fila(TIPO_FILA_PRIORITARIA)
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(5))
print(teste_fabrica.chama_cliente(8))
print(teste_fabrica.chama_cliente(10))

print(teste_fabrica.estatistica(EstatisticaResumida('06/04/2020', 182)))
print(teste_fabrica.estatistica(EstatisticaDetalhada('06/04/2020', 182)))
