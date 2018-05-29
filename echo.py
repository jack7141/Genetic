from Genetic import Genes as G
from random import random

class Ecosystem:
    def __init__(self, ge):
        self.generation = ge
        self.gene_list = self.initialize_gene()
        self.parents = []
        self.who_parents()
        self.none_parents_delete()
#유전자생성
    def initialize_gene(self):
        gene_list = []
        for i in range(30):#30번
            while True:
                temp = int(random()*1000000)
                if len(str(temp))==6:#길이
                    g = G(temp)    
                    gene_list.append(g)
                    break
      

        return gene_list
#부모 유전자 선택
    def who_parents(self):
        for i in range(2):#왜 2번돌리는가??
            temp = G(0)
            for j in range(30):
                # print(self.gene_list[j].status)
                # print(self.gene_list[j].similar)
                if temp.similar  < self.gene_list[j].similar and not self.gene_list[j] in self.parents :
                    temp = self.gene_list[j]
            
            self.parents.append(temp)                          

#부모 유전자를 제외하고 제거
    def none_parents_delete(self):
        for index, item in enumerate(self.gene_list):
            del item
            self.gene_list[index] = None
        self.gene_list= []            