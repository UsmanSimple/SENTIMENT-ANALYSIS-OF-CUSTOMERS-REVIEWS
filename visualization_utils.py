import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from textwrap import wrap

def histogram_density_plot(df : pd.DataFrame, target : str, var : str):
    fig, ax = plt.subplots(nrows=1, ncols=2,figsize = (20, 8))
    fig.suptitle(f'{target.title()} vs {var.title()}', fontsize=13)
    for i in df[target].unique():
        sns.distplot(df[df[target]==i][var], hist=True, kde=False, 
                    bins=10, hist_kws={"alpha":0.8}, 
                    axlabel="histogram", ax=ax[0])
        sns.distplot(df[df[target]==i][var], hist=False, kde=True, 
                    kde_kws={"shade":True}, axlabel="density",   
                    ax=ax[1])
    ax[0].grid(True)
    ax[0].legend(df[target].unique())
    ax[1].grid(True)
    plt.show()


def generate_wordcloud(text, title):
    wc = WordCloud(width=500, height=400, background_color='black', max_words = 100)
    wc = wc.generate(str(text))
    plt.figure(figsize =(20, 15), edgecolor='k', facecolor= 'k')
    plt.imshow(wc, interpolation='bilinear')
    plt.title('\n'.join(wrap(title, 20)), fontsize = 12)
    plt.axis('off')
    plt.tight_layout(pad = 0)
    plt.show()


    
def plot_ngram(texts: list, main_title, sub_titles=['Unigram Plot', 'Bigrams Plot', 'Trigrams Plot']):
    fig, axes = plt.subplots(figsize = (10,8), nrows=3, ncols=1)
    fig.suptitle(f'Most Frequents Words- {main_title.title()}')
    for val, ax, title in zip(texts, axes, sub_titles):
        val.set_index('Word').plot(kind = 'barh', title = title, ax = ax, legend =False).grid(axis='x')
        ax.set(ylabel = None)
        plt.tight_layout(pad= 0.3, w_pad= 0.4, h_pad=1.0)
        plt.show()






