"""DeepWalk illustrative example."""
'''
import networkx as nx
from karateclub.node_embedding.neighbourhood import DeepWalk

g = nx.newman_watts_strogatz_graph(100, 20, 0.05)

model = DeepWalk()

model.fit(g)

'''

import networkx as nx
from karateclub.node_embedding.neighbourhood import DeepWalk

#  创建一个Newman-Watts-Strogatz图
g = nx.newman_watts_strogatz_graph(100, 20, 0.05)

#  创建一个BoostNE对象
model = DeepWalk()

#  使用图进行拟合
model.fit(g)

#  获取节点嵌入
embedding = model.get_embedding()

#  打印节点嵌入
print("Node  embeddings:")
for node, embedding in enumerate(embedding):
    print(f"Node  {node}:  {embedding}")
