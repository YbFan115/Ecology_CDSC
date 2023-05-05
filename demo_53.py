# coding: utf-8
get_ipython().run_line_magic('ls', '')
import pandas as pd
get_ipython().run_line_magic('ls', '-t')
df1 = pd.read_csv("sub_fan_wikidata.csv")
df2 = pd.read_csv('sub_wiki.csv')
df1 = pd.read_csv("fan_wiki.csv")
df3 = pd.read_csv("sub_fan_wikidata.csv")
df1
df2
df3
