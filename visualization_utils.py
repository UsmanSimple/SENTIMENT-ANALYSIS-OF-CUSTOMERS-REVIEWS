import matplotlib.pyplot as plt
import seaborn as sns
def histogram_density_plot(df, target, var):
    fig, ax = plt.subplots(nrows=1, ncols=2)
    fig.suptitle(target, fontsize=12)
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