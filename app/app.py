import streamlit as st
from get_user_data import User
from custom_errors import UserNotFoundError

movie_genres = ['All',
                '(no genres listed)',
                'Action',
                'Adventure',
                'Animation',
                'Children',
                'Comedy',
                'Crime',
                'Documentary',
                'Drama',
                'Fantasy',
                'Film-Noir',
                'Horror',
                'IMAX',
                'Musical',
                'Mystery',
                'Romance',
                'Sci-Fi',
                'Thriller',
                'War',
                'Western'
                ]

given_movies = [{
    "title" : "deneme_movie_1",
    "movie_id": "12",
    "genre": ["Comedy"]
}]

#user_dbase =["12", "1", "13"]

def check_session_validity():
    if "valid_user" in st.session_state:
        return True
    return False

def main_app():
    # Set the page title and header
    st.set_page_config(page_title="Movie Recommender", page_icon="🤖")
    st.title("Streamflix 🎈")
    valid_user = check_session_validity()

    """
    Wanna chill and enjoy some movies?
    """

    with st.sidebar.form("recommend"):
        # Create a sidebar with a search field and a dropdown for filtering by genre
        user_id = st.text_input("Enter Spotlight user id", key="user")
        sub_btn = st.form_submit_button("Recommend!")
        st.session_state["user_id"] = user_id


    ##Check if user exists in our DB
    if sub_btn:
        user_obj = User(st.session_state["user_id"])
        try:
            user_obj.check_user()
        except UserNotFoundError as e:
            st.error(e)
        else:
            st.session_state["valid_user"] = True
            valid_user = True

    if valid_user:
        f"""#welcome {st.session_state['user_id']}"""

        # Get movies from backend
        movies = user_obj.get_recommended_movies
        #movies = given_movies
        st.sidebar.selectbox("Filter by genre", movie_genres, key="genre_box")

        # Use a list comprehension to filter the movies and TV shows based on the search term and genre
        filtered_movies_and_tv_shows = [
            movie for movie in movies
            if st.session_state["genre_box"] == "All" or movie["genre"] == st.session_state["genre_box"]
        ]

        # Display the filtered movies and TV shows as a list. Include rating button
        user_ratings = {}
        for movie in filtered_movies_and_tv_shows:
            user_ratings[movie["movie_id"]]= st.slider(movie["title"], min_value=0, max_value=5, key=f"{movie['title']}_slider")

        if st.button("Rate movies", key=f"rate_movies_btn"):
            for movie_id, rating in user_ratings:
                user_obj.post_movie_rating(movie_id, rating)

if __name__ == "__main__":
    main_app()