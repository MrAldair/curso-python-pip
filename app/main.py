import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  
  continent = input('Escoge un continente: ')

  data = list(filter(lambda item : item['Continent'] == continent, data))
  countries = list(map(lambda pais: pais['Country/Territory'], data))
  percentages = list(map(lambda porcentaje: porcentaje['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
 
  country = input("Digite un pais: ")
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__== '__main__':
  run()