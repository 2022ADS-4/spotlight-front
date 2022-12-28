import requests
from custom_errors import UserNotFoundError


class User:
    RECOMMENDER_URL = "http://127.0.0.1:8000"

    def __init__(self, user_id):

        self.user_id = user_id
    @property
    def get_recommended_movies(self):
        return requests.get(f"{self.RECOMMENDER_URL}/get_movies", params={"user_id":self.user_id}).json()

    def post_movie_rating(self, movie_id, rating):
        return requests.post(f"{self.RECOMMENDER_URL}/rating",
                      params={
                          "user_id": self.user_id,
                          "movie_id": movie_id,
                          "rating": rating
                      })

    @staticmethod
    def _convert_pandas_dataframe(in_json:dict):
        import pandas as pd
        return pd.DataFrame.from_dict(in_json)

    def check_user(self):
        if self.get_recommended_movies is None:
            raise UserNotFoundError("User id does not exist!")