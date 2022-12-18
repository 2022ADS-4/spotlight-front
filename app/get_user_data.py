import requests
from custom_errors import UserNotFoundError

class User:
    RECOMMENDER_URL = "http://127.0.0.1:8000"

    def __init__(self, user_id):
        self.data = {
            "user_id" : user_id,
        }
        self.user_data = requests.get(f"{self.RECOMMENDER_URL}/get_movies", params=self.data).json()
        print(self.user_data)
        self.user_id = user_id if self.user_data else None

        for key, value in self.user_data.items():
            self.__setattr__(key, value)
            self.data[key] = value

    def get_recommended_movies(self):
        return [
            {"title": "The Shawshank Redemption", "genre": "Drama"},
            {"title": "The Godfather", "genre": "Drama"},
            {"title": "Pulp Fiction", "genre": "Drama"},
            {"title": "The Dark Knight", "genre": "Action"},
            {"title": "The Prestige", "genre": "Thriller"},
            {"title": "The Hangover", "genre": "Comedy"},
            {"title": "The Office", "genre": "Comedy"},
            {"title": "Scream", "genre": "Horror"},
        ]

    def post_movie_rating(self, movie_id, rating):
        requests.post(f"{self.RECOMMENDER_URL}/rating",
                      params={
                          "movie_id" : movie_id,
                          "rating" : rating
                      })

    @staticmethod
    def _convert_pandas_dataframe(in_json:dict):
        import pandas as pd
        return pd.DataFrame.from_dict(in_json)

    def check_user(self):
        if self.user_id is None:
            raise UserNotFoundError("User id does not exist!")