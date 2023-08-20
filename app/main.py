import utils
import read_csv
import charts
import pandas as pd

def run():
  """""
  
  
  continent = input('Escoge un continente: ')

  data = list(filter(lambda item : item['Continent'] == continent, data))

  countries = list(map(lambda pais: pais['Country/Territory'], data))
  percentages = list(map(lambda porcentaje: porcentaje['World Population Percentage'], data))
  
  """
  df = pd.read_csv('./data.csv')
  df = df[df["Continent"] == "Africa"]

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('./data.csv')
  country = input("Escoge un país: ")
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__== '__main__':
  run()