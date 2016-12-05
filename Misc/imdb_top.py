#from lxml import parse
import pandas as pd
pd.options.display.max_rows=10
dfs = pd.read_html('http://www.imdb.com/chart/top')
print len(dfs)
for d in dfs:
  print "-"*65
  print d.head()

