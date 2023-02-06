# %% [markdown]
# # WWE WRESTLERS🤼‍♂️💥

# %% [markdown]
# * Libraries💻

# %%
import numpy as np
import pandas as pd
import datetime

# %% [markdown]
# * Importing the .csv file✅

# %%
wrestlers = pd.read_csv("/Users/lauurasarabia/Ironhack/projects/Project-2/data/data.csv")
wrestlers

# %% [markdown]
# * Dropping the columns which will not be used for the analysis🧨

# %%
wrestlers.drop(["link", "date_of_death", "cause_of_death"], axis=1, inplace=True)

# %% [markdown]
# * Changing date format in "date_of_birth" column in order to be able to filter by date📆

# %%
#Change date format from "mm/dd/YYYY" to "dd/mm/YYYY" and remove the "YYYY" as we won't use it
wrestlers['date_of_birth'] = pd.to_datetime(wrestlers['date_of_birth'], format="%m/%d/%Y")
wrestlers['DOB'] = wrestlers['date_of_birth'].dt.strftime("%d/%m")

#Add same year for all dates in order to be able to compare them
wrestlers['DOB'] = wrestlers['DOB'] + "/2023"

wrestlers['DOB'] = pd.to_datetime(wrestlers['DOB'], format="%d/%m/%Y")

# %% [markdown]
# * Let's find out which horoscope are they🧐

# %%
# Pass the conditions for each horoscope
conditions = [
    (wrestlers['DOB'] >= "2023-12-22") & (wrestlers['DOB'] <= "2023-01-19"),
    (wrestlers['DOB'] >= "2023-01-20") & (wrestlers['DOB'] <= "2023-02-18"),
    (wrestlers['DOB'] >= "2023-02-19") & (wrestlers['DOB'] <= "2023-03-20"),
    (wrestlers['DOB'] >= "2023-03-21") & (wrestlers['DOB'] <= "2023-04-19"),
    (wrestlers['DOB'] >= "2023-04-20") & (wrestlers['DOB'] <= "2023-05-20"),
    (wrestlers['DOB'] >= "2023-05-21") & (wrestlers['DOB'] <= "2023-06-20"),
    (wrestlers['DOB'] >= "2023-06-21") & (wrestlers['DOB'] <= "2023-07-22"),
    (wrestlers['DOB'] >= "2023-07-23") & (wrestlers['DOB'] <= "2023-08-23"),
    (wrestlers['DOB'] >= "2023-08-23") & (wrestlers['DOB'] <= "2023-09-22"),
    (wrestlers['DOB'] >= "2023-08-23") & (wrestlers['DOB'] <= "2023-10-22"),
    (wrestlers['DOB'] >= "2023-10-23") & (wrestlers['DOB'] <= "2023-11-21"),
    (wrestlers['DOB'] >= "2023-11-22") & (wrestlers['DOB'] <= "2023-12-21"),
    ]

values = [
    "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", 
    "Cancer", "Leo", "Virgo", "Libra", "Scorpio","Sagittarius",
    ]

wrestlers["Horoscope"] = np.select(conditions, values)
wrestlers



# %% [markdown]
# * Giving final touches to columns🪄

# %%
wrestlers = wrestlers.rename(columns={"name":"Name",
                                      "date": "Date",
                                      "reign":"Reign",
                                      "days":"Days",
                                      "event":"Event",
                                      "location":"Location",
                                      "belt":"Belt",
                                     })

# %%
wrestlers.head(10)

# %%
wrestlers['DOB'] = wrestlers['date_of_birth'].dt.strftime("%d/%m")

# %%
wrestlers.drop(columns='date_of_birth', inplace=True)

# %%
wrestlers.head(10)

# %%
wrestlers.to_csv('/Users/lauurasarabia/Ironhack/projects/Project-2/data/WWE_Wrestlers.csv')


