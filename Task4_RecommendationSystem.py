# Task 4 - Streamlit Movie Recommender (Flat Movie List on Homepage)
# CODSOFT AI Internship

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Load Movie Dataset
# ----------------------------
def load_movies():
    return pd.DataFrame({
        'MovieID': list(range(1, 18)),
        'Title': [
            'The Matrix', 'John Wick', 'Inception', 'The Notebook',
            'Interstellar', 'Titanic', 'Edge of Tomorrow', 'Gravity',
            '3 Idiots', 'Dangal', 'PK', 'Drishyam', 'Bahubali',
            'Chhichhore', 'Zindagi Na Milegi Dobara', 'Shershaah', 'Raazi'
        ],
        'Genre': [
            'Action Sci-Fi', 'Action Thriller', 'Sci-Fi Thriller', 'Romance Drama',
            'Sci-Fi Adventure', 'Romance Historical', 'Action Sci-Fi', 'Sci-Fi Thriller',
            'Comedy Drama College', 'Biography Sports Drama', 'Comedy Sci-Fi', 'Thriller Drama',
            'Action Fantasy', 'Drama College Comedy', 'Adventure Drama',
            'Biography War Action', 'Spy Thriller'
        ],
        'Description': [
            'A hacker discovers reality is a simulation and joins a rebellion.',
            'An ex-hitman comes out of retirement to hunt his enemies.',
            'A thief enters people’s dreams to steal secrets and plant ideas.',
            'A young couple falls in love during the 1940s despite obstacles.',
            'Explorers travel through a wormhole to save humanity.',
            'A tragic love story on a doomed ocean liner.',
            'A soldier relives the same day fighting aliens in a time loop.',
            'An astronaut fights to survive after a space accident.',
            'Two friends pursue engineering and question the Indian education system.',
            'A wrestler trains his daughters to become world champions in India.',
            'An alien stranded on Earth explores human beliefs and systems.',
            'A man creates a fake alibi to protect his family after a crime.',
            'A warrior prince battles for a kingdom in ancient India.',
            'A group of friends reunite and reflect on life and failures.',
            'Three friends go on a road trip that changes their lives.',
            'An army officer shows courage during the Kargil War.',
            'A young woman is recruited as a spy in enemy territory.'
        ]
    })

# ----------------------------
# Search by Genre
# ----------------------------
def search_by_genre(df, genre_query):
    genre_query = genre_query.lower()
    matched = df[df['Genre'].str.lower().str.contains(genre_query)]
    if matched.empty:
        return f"No movies found for genre: '{genre_query}'", []
    else:
        result = f"🎭 Movies in the genre: {genre_query.capitalize()}"
        return result, matched.to_dict(orient='records')

# ----------------------------
# Recommend by Movie Title
# ----------------------------
def recommend_by_title(df, similarity_matrix, title, top_n=5):
    if title not in df['Title'].values:
        return f"No such movie found: '{title}'", []

    index = df[df['Title'] == title].index[0]
    target_genre = df.loc[index, 'Genre']
    target_genre_set = set(target_genre.lower().split())

    similarity_scores = list(enumerate(similarity_matrix[index]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]

    result = f"🎬 Because you liked **{title}** (Genre: {target_genre}):"
    recommendations = []

    count = 0
    for i, score in sorted_scores:
        other_genre_set = set(df['Genre'][i].lower().split())
        genre_match = len(target_genre_set & other_genre_set)
        genre_confidence = round((genre_match / len(target_genre_set)) * 100, 1) if target_genre_set else 0

        recommendations.append({
            'Title': df['Title'][i],
            'Genre': df['Genre'][i],
            'Similarity': round(score * 100, 2),
            'GenreMatch': genre_confidence,
            'Description': df['Description'][i]
        })

        count += 1
        if count >= top_n:
            break

    return result, recommendations

# ----------------------------
# Display Movie Cards
# ----------------------------
def display_movies(movie_list):
    for movie in movie_list:
        with st.container():
            st.markdown(f"### 🎬 {movie['Title']}")
            st.markdown(f"**🎭 Genre:** {movie['Genre']}")
            if 'Similarity' in movie:
                st.markdown(f"**🤖 Similarity:** {movie['Similarity']}% | 🎯 Genre Match: {movie['GenreMatch']}%**")
            st.markdown(f"**📝 Description:** {movie['Description']}")
            st.markdown("---")

# ----------------------------
# Streamlit App
# ----------------------------
def main():
    st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
    st.title("🎥 AI Movie Recommendation System")
    st.markdown("Type a movie title or genre to get smart recommendations. Or scroll to browse all movies!")

    df = load_movies()
    tfidf_matrix = TfidfVectorizer(stop_words='english').fit_transform(df['Description'])
    similarity_matrix = cosine_similarity(tfidf_matrix)

    user_input = st.text_input("🔎 Search", placeholder="Try 'Action', 'Inception', or 'Comedy'")

    if user_input:
        if user_input in df['Title'].values:
            header, results = recommend_by_title(df, similarity_matrix, user_input)
        else:
            header, results = search_by_genre(df, user_input)

        st.subheader(header)
        if results:
            display_movies(results)
        else:
            st.info("No matches found.")
    else:
        st.subheader("📚 All Available Movies")
        all_movies = df.to_dict(orient='records')
        display_movies(all_movies)

if __name__ == "__main__":
    main()
