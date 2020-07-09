import pandas as pd
from somajo import SoMaJo


comments = []
df = pd.read_csv('comments.csv')
df = df.dropna(subset=['comment'])
df = df.reset_index(drop=True)

tokenizer = SoMaJo("de_CMC")
sentences = tokenizer.tokenize_text(df['comment'].tolist())
for sentence in sentences:
    comments.append(" ".join([token.text for token in sentence]))

df = pd.DataFrame(comments)

df.to_csv('comments_new.csv')
