import country_info as CountryInfo

print("Enter the country")
nation = input(":>> ")
CountryInfo(nation)

print("Captial: ", CountryInfo.capital())
print("Currency: ", CountryInfo.currencies())
print("Language: ", CountryInfo.languages())
print("Border: ", CountryInfo.borders())
print("Other names: ", CountryInfo.alt_spellings())