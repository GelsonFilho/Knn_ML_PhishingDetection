from sqlalchemy.sql.elements import conv

from dado import dado
from typing import List
import math


class knn:
    # Receber um dado não classificado (z),
    # o conjunto de dados classificados (X)
    # e o número de vizinhos (k);
    def __init__(self, k: int, conjunto_dados: List[dado]):
        self.__k__ = k
        self.__conjunto_dados__ = conjunto_dados

    def __metric_eclid__(self, new_dado: List[float], dado_clf: List[float]):
        somatorio: float = 0
        for carac_new_dado, carac_dado_clf in zip(new_dado, dado_clf):
            somatorio += math.pow((carac_new_dado - carac_dado_clf), 2)
        return math.sqrt(somatorio)

    def __next_to__(self):
        cnj_ordem = sorted(self.__conjunto_dados__, key=dado.get_distancia)
        print(cnj_ordem)
        return cnj_ordem[:self.__k__]

    def __most_rec__(self, dados_mais_proximos: List[dado]):
        dic_class = {}
        for close_data in dados_mais_proximos:
            if close_data.get_classe() in dic_class:
                dic_class[close_data.get_classe()] += 1
            else:
                dic_class[close_data.get_classe()] = 1
        return max(dic_class, key=dic_class.get)

    def executar(self, new_dado: dado):
        # Medir a distância de z para cada dado que já classificado;
        for dado_clf in self.__conjunto_dados__:
            distancia = self.__metric_eclid__(
                new_dado.get_atributos(), dado_clf.get_atributos())
            dado_clf.set_distancia(distancia)
        # Obter as k menores distâncias
        dados_mais_proximos = self.__next_to__()
        # Verificar a classe de cada um dos dados k dados de menor distância
        # e contar a quantidade de vezes que cada classe que aparece
        # Receber como resultado a classe mais recorrente
        classe = self.__most_rec__(dados_mais_proximos)
        # Classificar o novo dado com a classe mais recorrente
        new_dado.set_classe(classe)
