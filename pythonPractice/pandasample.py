# Three lines to make our compiler able to draw:
import sys
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/krishnanchandran/Downloads/data.csv')

df.plot()

plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig("viss.png")
sys.stdout.flush()
