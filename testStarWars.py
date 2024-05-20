from star_wars.src.star_wars_agent import StarWarAgent

class StarWarTester():
    def __init__(self):
        self.sWa = StarWarAgent()

    def get_all_movies(self):
        movieData = self.sWa.get_all_films()
        return movieData

    def get_specific_movie(self, idNumber):
        movieData = self.sWa.get_film_by_id(idNumber)
        return movieData
    
if __name__ == '__main__':
    StarWarTester()