# Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни,
# кількість жителів міста, поштовий індекс міста, телефонний код міста. Реалізуйте доступ до окремих полів (
# Інкапсуляція).

class City:
    def __init__(self, name: object, name_region: object, name_country: object, number_of_inhabitant: object,
                 postal_code_of_the_city: object,
                 city_code: object) -> object:
        self.__name = name
        self.__name_region = name_region
        self.__name_country = name_country
        self.__number_of_inhabitant = number_of_inhabitant
        self.__postal_code_of_the_city = postal_code_of_the_city
        self.__city_code = city_code

    def get_name(self):
        return self.__name

    def get_name_region(self):
        return self.__name_region

    def get_name_country(self):
        return self.__name_country

    def get_number_of_inhabitant(self):
        return self.__number_of_inhabitant

    def get_postal_code_of_the_city(self):
        return self.__postal_code_of_the_city

    def get_city_code(self):
        return self.__city_code


Sumy = City("Суми", "Сумська обл", "Україна", 250000, 40000, "+380542")

print("Name city:", Sumy.get_name())
print("Name region:", Sumy.get_name_region())
print("Name country:", Sumy.get_name_country())
print("Number of inhabitant:", Sumy.get_number_of_inhabitant())
print("Postal code of the city:", Sumy.get_postal_code_of_the_city())
print("City code:", Sumy.get_city_code())

# Завдання 2:
#
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів
# країни, телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція).

class Country:
    def __init__(self, name_country, the_name_of_the_continent, number_of_inhabitant, country_code, the_name_of_the_capital, the_name_of_the_countrys_cities):
        self.__name_country = name_country
        self.__the_name_of_the_continent = the_name_of_the_continent
        self.__number_of_inhabitant = number_of_inhabitant
        self.__country_code = country_code
        self.__the_name_of_the_capital = the_name_of_the_capital
        self.__the_name_of_the_countrys_cities = the_name_of_the_countrys_cities

    def get_name_country(self):
        return self.__name_country

    def get_the_name_of_the_continent(self):
        return self.__the_name_of_the_continent

    def get_number_of_inhabitant(self):
        return self.__number_of_inhabitant

    def get_country_code(self):
        return self.__country_code

    def get_the_name_of_the_capital(self):
        return self.__the_name_of_the_capital

    def get_the_name_of_the_countrys_cities(self):
        return self.__the_name_of_the_countrys_cities

Ukraine = Country("Україна", "Європа", "41 167 335", "+380", "Київ", "Львів, Херсон, Одеса, Харків")

print("Name country:", Ukraine.get_name_country())
print("The name of the continent:", Ukraine.get_the_name_of_the_continent())
print("Number of inhabitant:", Ukraine.get_number_of_inhabitant())
print("Country code:", Ukraine.get_country_code())
print("The name of the capital:", Ukraine.get_the_name_of_the_capital())
print("The name of the country's cities:", Ukraine.get_the_name_of_the_countrys_cities())