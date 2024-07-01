import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level')
plt.scatter(Year, CSIRO Adjusted Sea Level)
plt.show()
    # Create first line of best fit
slope, intercept = np.polyfit(Year, CSIRO Adjusted Sea Level, 1)
plt.scatter(Year, CSIRO Adjusted Sea Level)
plt.plot(Year, slope * Year + intercept)
    # Create second line of best fit


    # Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
