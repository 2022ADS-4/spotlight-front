import streamlit as st

movie_genres = [
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

def run_streamlit():
    st.set_page_config(page_title="Movie Recommender", page_icon="🤖")
    with st.form("Recommend me!"):
        st.header("Enter below info")
        user_id = st.text_input("Enter User id: ")
        genre = st.selectbox("Select movie genre", movie_genres)
        submit_btn = st.form_submit_button("Recommend me!")

        if submit_btn:
            with st.spinner('Wait for it...'):
                from get_movies import UIMovieRecommendation
                data_input = {
                "user_id": user_id,
                "genre": genre
            }
                recommended_movies = UIMovieRecommendation(
                    data=data_input
                ).get_recommended_movies()

            st.table(recommended_movies)


if __name__ == "__main__":
    run_streamlit()
