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


def main_app():
    # Set the page title and header
    st.set_page_config(page_title="Movie Recommender", page_icon="🤖")
    st.title("Streamflix 🎈")

    """
    Wanna chill and enjoy some movies?
    """

    with st.sidebar.form("recommend"):
        # Create a sidebar with a search field and a dropdown for filtering by genre
        user_id = st.text_input("Enter Spotlight user id", key="user")
        sub_btn = st.form_submit_button("Recommend!")
        st.session_state["user_id"] = user_id

        valid_user = False

    ##Check if user exists in our DB
    if sub_btn:
        user_obj = User(st.session_state["user_id"])
        try:
            user_obj.check_user()
        except UserNotFoundError as e:
            st.error(e)
        else:
            valid_user = True
            st.session_state
            st.session_state["selected_genre"] = "All"

    if valid_user:
        f"""#welcome {st.session_state['user_id']}"""

        # Get movies from backend
        movies = user_obj.get_recommended_movies
        st.sidebar.selectbox("Filter by genre", movie_genres, key="genre_box")

        # Use a list comprehension to filter the movies and TV shows based on the search term and genre
        filtered_movies_and_tv_shows = [
            movie for movie in movies
            if st.session_state["selected_genre"] == "All" or movie["genre"] == st.session_state["selected_genre"]
        ]

        # Display the filtered movies and TV shows as a list. Include rating button
        for movie in filtered_movies_and_tv_shows:
            st.slider(movie["title"], min_value=0, max_value=5, key=f"{movie['title']}_slider")
            st.button("Rate this movie", key=f"rate_{movie['title']}_btn")


if __name__ == "__main__":
    main_app()