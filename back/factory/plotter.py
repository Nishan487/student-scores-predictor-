import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class Plotter:
    @staticmethod
    def plot(df,save_path="static/plot.png"):
        df.plot(x='Hours', y='Scores', style='o')
        plt.title('Hours vs Percentage')
        plt.xlabel('Hours Studied')
        plt.ylabel('Percentage Score')
        plt.savefig(save_path)
        plt.close()