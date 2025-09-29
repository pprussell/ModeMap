#!/usr/bin/env python
print("")
print("Importing Libraries...")
from matplotlib import pyplot as plt
import pandas as pd
from smtgplot.formatting import set_formatting
from os.path import exists as path_exists

if not path_exists("ModeMap_PostProcess.csv"):
    print("\nUnable to find ModeMap_PostProcess.csv")
    exit()

print("\nLoading results...")
results = pd.read_csv("ModeMap_PostProcess.csv", header=1)
print(results)

set_formatting()

print("\nPlotting...")
ax = results.plot(kind="line", x="Q [amu^1/2 A]", y="dU(Q) [meV]", legend=False)
ax = results.plot(kind="scatter", x="Q [amu^1/2 A]", y="dU(Q) [meV]", ax=ax)
plt.savefig("ModeMap.pdf")
plt.show()

print("Plot saved to ModeMap.pdf")
exit()