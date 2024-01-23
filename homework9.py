# Hello
# Task_1

# class City:
#     def __init__(self, name, region, country, population, post_code, phone_code):
#         self.__name = name
#         self.__region = region
#         self.__country = country
#         self.__population = population
#         self.__post_code = post_code
#         self.__phone_code = phone_code
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def region(self):
#         return self.__region
#
#     @property
#     def country(self):
#         return self.__country
#
#     @property
#     def population(self):
#         return self.__population
#
#     @property
#     def post_code(self):
#         return self.__post_code
#
#     @property
#     def phone_code(self):
#         return self.__phone_code
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @region.setter
#     def region(self, region):
#         self.__region = region
#
#     @country.setter
#     def country(self, country):
#         self.__country = country
#
#     @population.setter
#     def population(self, population):
#         self.__population = population
#
#     @post_code.setter
#     def postal_code(self, post_code):
#         self.__post_code = post_code
#
#     @phone_code.setter
#     def phone_code(self, phone_code):
#         self.__phone_code = phone_code
#
# some_city = City("Kyiv", "Kyiv region", "Ukraine", 123456, "123456", "+380")
# print(f"The city name is {some_city}")
# print(f"Region: {some_city.region}")
# print(f"Country: {some_city.country}")
# print(f"Population: {some_city.population}")
# print(f"Postal code: {some_city.post_code}")
# print(f"Phone code: {some_city.phone_code}")
#
# some_city.region = "Lvivska"
# print(f"Region after change: {some_city.region}")


## Task_2

# class Country:
#     def __init__(self, name, name_of_continent, population, phone_code, capital, name_of_countries):
#         self.__name = name
#         self.__name_of_continent = name_of_continent
#         self.__population = population
#         self.__phone_code = phone_code
#         self.__capital = capital
#         self.__name_of_countries = name_of_countries
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def name_of_continent(self):
#         return self.__name_of_continent
#
#     @property
#     def population(self):
#         return self.__population
#
#     @property
#     def phone_code(self):
#         return self.__phone_code
#
#     @property
#     def capital(self):
#         return self.__capital
#
#     @property
#     def name_of_countries(self):
#         return self.__name_of_countries
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name_of_continent.setter
#     def name_of_continent(self, name_of_continent):
#         self.__name_of_continent = name_of_continent
#
#     @population.setter
#     def population(self, population):
#         self.__population = population
#
#     @phone_code.setter
#     def phone_code(self, phone_code):
#         self.__phone_code = phone_code
#
#     @capital.setter
#     def capital(self, capital):
#         self.__capital = capital
#
#     @name_of_countries.setter
#     def name_of_countries(self, name_of_countries):
#         self.__name_of_countries = name_of_countries
#
#
# country1_cities = ["Kyiv", "Lviv", "Sumy"]
# country1 = Country("Ukraine", "Europe", 7654321, "+380123456789", "Kyiv", country1_cities)
#
# print(f"Name of country: {country1.name}")
# print(f"Name of continent: {country1.name_of_continent}")
# print(f"Population: {country1.population}")
# print(f"Phone code: {country1.phone_code}")
# print(f"Capital: {country1.capital}")
# print(f"Cities: {country1.name_of_countries}")
#
# country1.name = "Ukraine"
# country1.population = 8765432
# country1.name_of_countries = ["Kyiv", "Kharkiv", "Lviv"]
#
# print(f"New name of country: {country1.name}")
# print(f"New population: {country1.population}")
# print(f"New cities: {country1.name_of_countries}")
