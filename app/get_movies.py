import tempfile
import requests
from custom_errors import UserNotFoundError

class UIMovieRecommendation:
    RECOMMENDER_URL = "http://127.0.0.1:8000/get_movies"
    def __init__(self, data:dict):
        self.data = data

    def get_recommended_movies(self):
        ##send post request to recommender
        response = requests.get(
            self.RECOMMENDER_URL, params=self.data)

        response_json = response.json()
        self.check_user(response_json)

        return self._convert_pandas_dataframe(response_json)

    @staticmethod
    def _convert_pandas_dataframe(in_json:dict):
        import pandas as pd
        return pd.DataFrame.from_dict(in_json)

    @staticmethod
    def check_user(response:dict):
        if all([None in value for value in list(response.values())]):
            raise UserNotFoundError("User id does not exist!")