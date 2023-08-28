import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def regression_for_attribute(dataFrame = pd.DataFrame, attribute = str):
    data = dataFrame

    attr = np.array(data[[attribute]]).reshape(-1)
    year = np.array(data[["year"]]).reshape(-1)

    slope, intercept, r_value, p_value, std_err = stats.linregress(year, attr)
    

    plt.figure(figsize = (15, 7))
    plt.scatter(year, attr, s = 2, color = "g")
    plt.xlabel("rok vydání")
    plt.ylabel(attribute)
    plt.axline((0, intercept), slope=slope)

    plt.xlim([min(year) - 1 ,max(year) + 1])
    plt.ylim([min(attr) * 0.9, max(attr) * 1.1])

    plt.figtext(0.02,0.9, f"koeficient determinace: {r_value * r_value:.3f}\np-hodnota: {p_value:.7f}\nsklon: {slope:.3f}")

    plt.savefig(attribute)
    plt.show()

with open('Best Songs on Spotify from 2000-2023.csv', encoding="utf8") as file:
    data = pd.read_csv(file, delimiter=';')
    data_length = len(data)

    # filtrace dat
    data = data.loc[data["year"] >= 2000]
    data = data.loc[data["duration"] < 400]

    filtered_data_lenght = len(data)

    print(f"kolik dat se vyfiltrovalo: {data_length - filtered_data_lenght}, to je {(1-filtered_data_lenght/data_length)*100:2f} %")

    regression_for_attribute(data, "dB")
    regression_for_attribute(data, "duration")
    regression_for_attribute(data, "valence")
