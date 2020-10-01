import pandas as pd
covid_df = pd.read_csv('covidCasesByCounty.csv')


def covid_cases_by_state(state_abr):
  cases_by_county = covid_df.iloc[:, 4:].set_index([covid_df['County Name'], covid_df["State"]])
  total_cases_by_county = cases_by_county.sum(axis=1)
  total_county_cases_by_state = total_cases_by_county[:,state_abr]
  return total_county_cases_by_state

def cases_by_state_over_time(state_abr):
  cases_by_state = covid_df.iloc[:, 4:].set_index(covid_df['State'])
  state_cases = cases_by_state.groupby('State').sum()
  state_cases_by_date = state_cases.loc[state_abr]
  return state_cases_by_date

covid_cases_by_state('RI')
cases_by_state_over_time("RI")
