import matplotlib.pyplot as plt
import seaborn as sns

def bp_histogram(df):
    '''
    Ritar ett histogram över blodtryck.
    '''
    plt.hist(df["systolic_bp"], bins=20)
    plt.xlabel("Blodtryck")
    plt.ylabel("Frekvens")
    plt.title("Histogram av blodtryck")
    plt.show()

def bp_vs_age(df):
    '''
    Visar sambandet mellan ålder och blodtryck
    med en enkel regressionslinje.
    '''
    sns.regplot(data=df, x="age", y="systolic_bp")
    plt.title("Ålder och blodtryck")
    plt.show()
