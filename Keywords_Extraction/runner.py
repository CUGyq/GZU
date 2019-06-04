#! -*- coding: utf-8 -*-
#date 13/5/2019
from DataProcess import processData
from ScoreCount import Ranking
from Graph import Graph
def main(inputsText,fname,alpha,beta,gamma,K):
    '''

    :param inputsText: 输入的一段文本
    :param fname:停用词文件
    :param alpha
    :param beta
    :param gamma
    :param K :topK keywords
    :return:
    '''

    wordsall_list=processData(inputsText,fname).process()
    graph=Graph(wordsall_list)
    G=graph.buildGraph()  #构建词图
    graph.VisionGraph() #可视化词图
    sorted_InteScore=Ranking(G,alpha,beta,gamma).integrateScore()
    topK=[sI[0] for sI in sorted_InteScore[0:K]]
    print("top K:",topK)
fname="stopwords.txt"
inputsText="昨天17时许，云南省罗平县交通局副局长张敢在办公室被一男子砍杀，身中数刀，经抢救无效后死亡，犯罪嫌疑人已被警方成功抓获。 据了解，行凶男子为钟山乡某学校一名教师，初步判断为情感纠纷。由于案情重大，罗平县公安局刑侦大队已立案侦查。截至发稿时，民警仍在现场勘查。"
main(inputsText,fname,0.1,0.1,0.8,20)
