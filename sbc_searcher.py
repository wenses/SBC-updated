import spacy
from tqdm import tqdm
import pandas as pd
from rank_bm25 import BM25Okapi
pd.set_option('display.max_colwidth',1)
nlp=spacy.load('en_core_web_sm')
df=pd.read_csv('sbc-b1.csv')

text_list=df.Name.str.lower().values
tok_text=[]

for doc in tqdm(nlp.pipe(text_list, disable=['tagger','parser','ner'])):
    tok=[t.text for t in doc if t.is_alpha]
    tok_text.append(tok)

bm25=BM25Okapi(tok_text)
query=str(input('Search SBC: '))
tokenized_query=query.lower().split(' ')
import time
t0=time.time()
results=bm25.get_top_n(tokenized_query, df.Name.values, n=3)
t1=time.time()

print(f'searched 7 iterations in {round(t1-t0)} seconds \n')

for i in results:
    print(results)