# coding: utf-8
get_ipython().run_line_magic('cd', 'reddit_wiki_ecology/')
import pandas as pd
df1 = pd.read_csv("sub_fan_wikidata.csv")
df1['subreddit'] = 's-' + df1['subreddit']
df1['fandom'] = 'f-' + df1['fandom']
df1
get_ipython().run_line_magic('ls', '-t')
df2 = pd.read_csv("sub_wiki.csv")
df2
df2['subreddit'] = 's-' + df2['subreddit']
df2['page_titleRO'] = 'w-' + df2['page_titleRO']
df2
df3 = pd.read_csv('fan_wiki.csv')
df3['fandom'] = 'f-' + df3['fandom']
df3['page_titleRO'] = 'w-' + df3['page_titleRO']
df3
df_sub_fan = df1
df_sub_wiki = df2
df_fan_wiki = df3
df_fan_wiki 
from igraph import Graph
all_nodes = set(df_sub_fan['subreddit']) | set(df_sub_fan['fandom']) | set(df_sub_wiki['page_titleRO']) | set(df_sub_wiki['subreddit']) | set(df_fan_wiki['page_titleRO']) | set(df_fan_wiki['fandom'])
g.add_vertices(list(all_nodes))
g = Graph()
g.add_vertices(list(all_nodes))
for _, row in df_sub_fan.iterrows():
        g.add_edge(row['subreddit'], row['fandom'])
        
for _, row in df_sub_wiki.iterrows():
        g.add_edge(row['subreddit'], row['page_titleRO'])
        
for _, row in df_fan_wiki.iterrows():
        g.add_edge(row['fandom'], row['page_titleRO'])
        
g.components()
clusters = [ cls for cls in g.components() ]
cluster_len = [ len(cls) for cls in g.components() ]
pd.Series(cluster_len).value_counts()
graph = igraph.Graph.Read_GraphML("ecology_1.graphml")
import igraph
graph = igraph.Graph.Read_GraphML("ecology_1.graphml")
clusters_1 = [ cls for cls in graph.components() ]
cluster_len_1 = [ len(cls) for cls in g.components() ]
pd.Series(cluster_len_1).value_counts()
cluster_len_1 = [ len(cls) for cls in graph.components() ]
pd.Series(cluster_len_1).value_counts()
