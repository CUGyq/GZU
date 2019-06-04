#! -*- coding: utf-8 -*-
#date 13/5/2019
import networkx as nx
import matplotlib.pyplot as plt
class Graph(object):
    def __init__(self,words_list):
        """
        :param words_list:
        """
        self.words_list =words_list

    def buildGraph(self):
        G=nx.Graph()
        words=[]
        for li in self.words_list:
            words.extend(li)
        count={}  #词频字典
        for w in set(words):
            count[w]=words.count(w)
        G.add_nodes_from(words)
        print(self.words_list)
        for li in self.words_list:
            for i,node1 in enumerate(li):
                for j in range(i+1,len(li)):
                    node2=li[j]
                    print((node1,node2))
                    if node1!=node2:
                        if not G.has_edge(node1,node2):
                            G.add_edge(node1,node2,weight=1.0)
                        else:
                            G[node1][node2]['weight']+=1.0
                    else:
                        pass
        print(G.edges(data=True))
        for u,v,d in G.edges(data=True):
            G[u][v]['weight']=1/2*((d['weight']/count[u])+(d['weight']/count[u]))
        print(count)
        print(G.edges(data=True))
        return G
    def VisionGraph(self):
        G=self.buildGraph()
        pos = nx.random_layout(G)
        nx.draw_networkx_nodes(G,pos,node_color='y',node_size=500)
        nx.draw_networkx_edges(G,pos,width=1) #此处默认为黑色
        nx.draw_networkx_labels(G, pos)
        plt.savefig('picture.png',dpi=300)
        plt.show()
