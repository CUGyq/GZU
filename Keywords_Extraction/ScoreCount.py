#! -*- coding: utf-8 -*-
#date 13/5/2019
import networkx as nx
class Ranking(object):
    def __init__(self,G,alpha,beta,gamma):
        '''

        :param G: 词图
        :param alpha: 度中心性权重系数
        :param beta: 介数中心性权重系数
        :param gamma: 特征向量中心性权重系数
        '''
        self.G=G
        self.alpha=alpha
        self.beta=beta
        self.gamma=gamma
    def degree_centrality(self):
        degree_centrality_dict=nx.degree_centrality(self.G)
        return degree_centrality_dict

    def betweeness_centrality(self):
        betweenness_centrality_dict = nx.betweenness_centrality(self.G,weight='weight')
        return betweenness_centrality_dict

    def eigenvector_centrality(self):
        eigenvector_centrality_dict=nx.eigenvector_centrality(self.G,weight='weight')
        return eigenvector_centrality_dict

    def integrateScore(self):
        degree_centrality_dict=self.degree_centrality()
        betweenness_centrality_dict=self.betweeness_centrality()
        eigenvector_centrality_dict=self.eigenvector_centrality()
        nodes=self.G.nodes
        InteScore={} #综合特征值
        for node in nodes:
            InteScore[node]=self.alpha*degree_centrality_dict[node]+self.beta*betweenness_centrality_dict[node]\
                            +self.gamma*eigenvector_centrality_dict[node]
        factor=sum(list(InteScore.values()))
        for k,v in InteScore.items():
            InteScore[k]=v*factor

        # 按照综合特征值降序排序,类型为[(node1,value1),(node2,value2).....]
        sorted_InteScore=sorted(InteScore.items(), key=lambda item: item[1], reverse=True)
        for i,item in enumerate(sorted_InteScore):
            if len(item[0])<2:
                del sorted_InteScore[i]
        return sorted_InteScore