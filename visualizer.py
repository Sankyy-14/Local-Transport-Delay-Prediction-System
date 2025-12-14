import matplotlib.pyplot as plt

def plot_delay_by_route(df):
    df.groupby('RouteID')['Delayed'].mean().plot(kind='bar')
    plt.show()
