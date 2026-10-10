from collections import Counter

inventors = [
    { 'first': 'Albert', 'last': 'Einstein', 'year': 1879, 'passed': 1955 },
    { 'first': 'Isaac', 'last': 'Newton', 'year': 1643, 'passed': 1727 },
    { 'first': 'Galileo', 'last': 'Galilei', 'year': 1564, 'passed': 1642 },
    { 'first': 'Marie', 'last': 'Curie', 'year': 1867, 'passed': 1934 },
    { 'first': 'Johannes', 'last': 'Kepler', 'year': 1571, 'passed': 1630 },
    { 'first': 'Nicolaus', 'last': 'Copernicus', 'year': 1473, 'passed': 1543 },
    { 'first': 'Max', 'last': 'Planck', 'year': 1858, 'passed': 1947 },
    { 'first': 'Katherine', 'last': 'Blodgett', 'year': 1898, 'passed': 1979 },
    { 'first': 'Ada', 'last': 'Lovelace', 'year': 1815, 'passed': 1852 },
    { 'first': 'Sarah E.', 'last': 'Goode', 'year': 1855, 'passed': 1905 },
    { 'first': 'Lise', 'last': 'Meitner', 'year': 1878, 'passed': 1968 },
    { 'first': 'Hanna', 'last': 'Hammarström', 'year': 1829, 'passed': 1909 }
]

people = [
        'Bernhard, Sandra', 'Bethea, Erin', 'Becker, Carl', 'Bentsen, Lloyd', 'Beckett, Samuel', 'Blake, William', 'Berger, Ric', 'Beddoes, Mick', 'Beethoven, Ludwig',
        'Belloc, Hilaire', 'Begin, Menachem', 'Bellow, Saul', 'Benchley, Robert', 'Blair, Robert', 'Benenson, Peter', 'Benjamin, Walter', 'Berlin, Irving',
        'Benn, Tony', 'Benson, Leana', 'Bent, Silas', 'Berle, Milton', 'Berry, Halle', 'Biko, Steve', 'Beck, Glenn', 'Bergman, Ingmar', 'Black, Elk', 'Berio, Luciano',
        'Berne, Eric', 'Berra, Yogi', 'Berry, Wendell', 'Bevan, Aneurin', 'Ben-Gurion, David', 'Bevel, Ken', 'Biden, Joseph', 'Bennington, Chester', 'Bierce, Ambrose',
        'Billings, Josh', 'Birrell, Augustine', 'Blair, Tony', 'Beecher, Henry', 'Biondo, Frank'
]
filtered_inventors = []
inventors_by_name = []
inventor_birth_dates = []
inventor_death_dates = []
inventors_sorted_by_age = []
for inventor in inventors:
    if 1500 <= inventor['year'] < 1600:
        filtered_inventors.append(inventor)
    else:
        pass
    inventors_by_name.append(f"{inventor['first']} {inventor['last']}")
    inventor_birth_dates.append(inventor['year'])
    inventor_death_dates.append(inventor['passed'])
print(filtered_inventors)
print(inventors_by_name)
inventor_birth_dates.sort()
print(inventor_birth_dates)
for year in inventor_birth_dates:
    for inventor in inventors:
        if inventor['year'] == year:
            inventors_sorted_by_age.append(inventor)
print(inventors_sorted_by_age)
inventor_combined_age = 0
inventor_ages = []
for i in range(len(inventors)):
    inventor_combined_age += (inventor_death_dates[i] - inventor_birth_dates[i])
    inventor_ages.append(inventors[i]['passed'] - inventors[i]['year'])
print(f"The inventors lived for a combined total of {inventor_combined_age} years.")
inventor_ages.sort()
inventors_by_years_lived = []
for age in inventor_ages:
    for inventor in inventors:
        if inventor['passed'] - inventor['year'] == age:
            inventors_by_years_lived.append(inventor)
print(inventors_by_years_lived)
boulevards = ["Boulevard Auguste-Blanqui", "Boulevard Barbes", "Boulevard Beaumarchais", "Boulevard de l'Amiral-Bruix", "Boulevard Mortier", "Boulevard Poniatowski", "Boulevard Soult", "Boulevard des Capucines", "Boulevard de la Chapelle", "Boulevard de Clichy", "Boulevard du Crime", "Boulevard du General-d'Armee-Jean-Simon", "Boulevard Haussmann", "Boulevard de l'Hopital", "Boulevard des Italiens", "Boulevard Lefebvre", "Boulevard de la Madeleine", "Boulevard de Magenta", "Boulevard Malesherbes", "Boulevard Marguerite-de-Rochechouart", "Boulevard Montmartre", "Boulevard du Montparnasse", "Boulevard Raspail", "Boulevard Richard-Lenoir", "Boulevard Saint-Germain", "Boulevard Saint-Michel", "Boulevard de Sebastapol", "Boulevard de Strasbourg", "Boulevard du Temple", "Boulevard Voltaire", "Boulevard Hippolyte-Marques"]
de_boulevards = []
for boulevard in boulevards:
    if 'de' in boulevard:
        de_boulevards.append(boulevard)
print(de_boulevards)
people.sort()
print(people)
data = ['car', 'car', 'truck', 'truck', 'bike', 'walk', 'car', 'van', 'bike', 'walk', 'car', 'van', 'car', 'truck' ]
data_tally = Counter(data)
print(data_tally)