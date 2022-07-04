import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def mean_std_cal(filepath):
       file_df = pd.read_csv(filepath, sep=",", header=0)
       Sample_Name = file_df["Sample Name"].unique()
       Condition_Name = file_df["Target Name"].unique()
       cal_df = pd.DataFrame()
       columns = list(cal_df)

       for Sample in Sample_Name:
              for Condition in Condition_Name:
                     mean = file_df.loc[(file_df["Sample Name"] == Sample)
                                        & (file_df["Target Name"] == Condition)]["Cт"].mean
                     std = file_df.loc[(file_df["Sample Name"] == Sample)
                                       & (file_df["Target Name"] == Condition)]["Cт"].std()

                     temp_dict = {
                            "sample": Sample,
                            "condition": Condition,
                            "mean": mean,
                            "std": std
                     }

                     cal_df = cal_df.append([temp_dict], ignore_index=True)
       cal_df = cal_df.dropna()

'''
def diff_cal(cal_df):
       for sample in cal_df["sample"]:
              sample["diluted 1:2 (D)"]
              sample["cut (M)"]
              sample["un-cut (C)"]
'''


#variables preperation
filepath = 'example_table.csv'
Title = 'title'
Y_lable = 'y-Lable'
mean_std_cal(filepath)

# Enter raw data
aluminum = np.array([6.4e-5 , 3.01e-5 , 2.36e-5, 3.0e-5, 7.0e-5, 4.5e-5, 3.8e-5, 4.2e-5, 2.62e-5, 3.6e-5])
copper = np.array([4.5e-5 , 1.97e-5 , 1.6e-5, 1.97e-5, 4.0e-5, 2.4e-5, 1.9e-5, 2.41e-5 , 1.85e-5, 3.3e-5 ])
steel = np.array([3.3e-5 , 1.2e-5 , 0.9e-5, 1.2e-5, 1.3e-5, 1.6e-5, 1.4e-5, 1.58e-5, 1.32e-5 , 2.1e-5])

# Calculate the average
Aluminum_mean = np.mean(aluminum)
Copper_mean = np.mean(copper)
Steel_mean = np.mean(steel)


# Calculate the standard deviation
aluminum_std = np.std(aluminum)
copper_std = np.std(copper)
steel_std = np.std(steel)

# Create lists for the plot
materials = ['Aluminum', 'Copper', 'Steel']
x_pos = np.arange(len(materials))
CTEs = [Aluminum_mean, Copper_mean, Steel_mean]
error = [aluminum_std, copper_std, steel_std]

# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos,
       CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       color='black',
       capsize=10)
ax.set_ylabel(Y_lable)
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.set_title(Title)
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()


