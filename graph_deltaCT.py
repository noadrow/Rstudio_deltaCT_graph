import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

# This script calculate mean values and standart deviation for each sample and condition
# Then it calculate the difference to the control condition for each sample
# and plot the results

# The first argument to run the script is the file location\name
# the second argument is the control condition name
# the rest of the argument are all the other conditions
# NOTE: It's important to keep the notation of condition the same as in the "Target name" column


#ADD: Undetermined cleanup

def mean_std_cal(filepath):
       file_df = pd.read_csv(filepath, sep=",", header=0)
       samples = file_df["Sample Name"].unique()
       Condition_Name = file_df["Target Name"].unique()
       cal_df = pd.DataFrame()
       columns = list(cal_df)

       for Sample in samples:
              for Condition in Condition_Name:
                     mean = pd.to_numeric(file_df.loc[(file_df["Sample Name"] == Sample)
                                        & (file_df["Target Name"] == Condition)]["Cт"]).mean()
                     std = pd.to_numeric(file_df.loc[(file_df["Sample Name"] == Sample)
                                       & (file_df["Target Name"] == Condition)]["Cт"]).std()

                     temp_dict = {
                            "sample": Sample,
                            "condition": Condition,
                            "mean": mean,
                            "std": std
                     }

                     cal_df = cal_df.append([temp_dict], ignore_index=True)
       cal_df = cal_df.dropna()
       return cal_df, samples

def diff_cal(cal_df,conditions,samples):
       results_df = pd.DataFrame()
       for sample in samples:
              for i,condition in enumerate(conditions):
                     if (i==0):
                            Csample_mean = cal_df.loc[(cal_df["sample"] == sample) &
                                                      (cal_df["condition"] == conditions[0])]['mean']
                            Csample_std = cal_df.loc[(cal_df["sample"] == sample) &
                                                     (cal_df["condition"] == conditions[0])]['std']
                     else:
                            conditionValue_mean = cal_df.loc[(cal_df["sample"] == sample) &
                                                             (cal_df["condition"] == condition)]['mean']
                            conditionValue_std = cal_df.loc[(cal_df["sample"] == sample) &
                                                            (cal_df["condition"] == condition)]['std']


                            diff_mean = conditionValue_mean.values - Csample_mean.values
                            diff_std = Csample_std.values + conditionValue_std.values

                            if (len(diff_mean)==1 & len(diff_std)==1):
                                   temp_dict = {
                                          "sample": sample,
                                          "condition": condition,
                                          "diff_mean": diff_mean[0],
                                          "diff_std": diff_std[0]
                                   }
                                   results_df = results_df.append([temp_dict], ignore_index=True)

       return results_df

def plot_CT(samples,conditions,results_df):
       for i,sample in enumerate(samples):
              x_pos = np.arange(len(conditions) - 1)

              CTEs = results_df.loc[results_df["sample"]==sample]["diff_mean"].values.tolist()
              error = results_df.loc[results_df["sample"]==sample]["diff_std"].values.tolist()

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

              ax.set_ylabel("delta_CT")
              ax.set_xticks(x_pos)
              ax.set_xticklabels(conditions[1:])
              ax.set_title(sample+" Difference To Control")
              ax.yaxis.grid(True)

              # Save the figure and show
              plt.tight_layout()
              plt.savefig(sample.replace("/","_")+"_bar_plot_with_error_bars'.png")
              plt.show()


#Variables Preparation
filepath = sys.argv[1]
#NOTE: control should be the first condition
conditions = sys.argv[2:]
#example_table.csv "un-cut (C)" "diluted 1:2 (D)" "cut (M)"

#create mean and standart deviation for duplecates
cal_df,samples = mean_std_cal(filepath)
#create difference of mean value to control
results_df = diff_cal(cal_df,conditions,samples)
#plot for each sample
plot_CT(samples,conditions,results_df)
