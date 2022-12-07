import tempfile
import requests

class UIMovieRecommendation:
    RECOMMENDER_URL = "http://127.0.0.1:8000/get_movies"
    def __init__(self, data:dict):
        self.data = data

    def get_recommended_movies(self):
        ##send post request to recommender
        response = requests.get(
            self.RECOMMENDER_URL, params=self.data)

        return self._convert_pandas_dataframe(response.json())

    @staticmethod
    def _convert_pandas_dataframe(in_json:dict):
        import pandas as pd
        return pd.DataFrame.from_dict(in_json)

    """def save_user_entry(self): #Artifact
        import json
        with open(self.user_json_out, "w") as j:
            j.write(json.dumps(self.data, indent=4)
                    )"""