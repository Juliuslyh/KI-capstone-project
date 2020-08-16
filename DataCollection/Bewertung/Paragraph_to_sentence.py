import pandas as pd
from somajo import SoMaJo
import os

def Para_to_Sentence():
    comments = []
    df = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd()))+'/data/'
                            +'comments.csv')
    df = df.dropna(subset=['comment'])
    df = df.reset_index(drop=True)

    tokenizer = SoMaJo("de_CMC")
    sentences = tokenizer.tokenize_text(df['comment'].tolist())
    for sentence in sentences:
        comments.append(" ".join([token.text for token in sentence]))

    df = pd.DataFrame(comments)

    df.to_csv(os.path.abspath(os.path.dirname(os.getcwd()))+'/data/'
                            +'comments_new.csv')
