# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


class Movie: 
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
        print("title:", self.title, "director:", self.director, "budget:", self.budget,"USD")

    def wasExpensive(self):
        if self.budget > 100000000:
            print(True)
        if self.budget < 100000000:
            print(False)


firstMovie = Movie("Titanic","James Cameron", 200000000)
firstMovie.wasExpensive()

secondMovie = Movie("Toy Story","John Lasseter", 30000000)
secondMovie.wasExpensive()