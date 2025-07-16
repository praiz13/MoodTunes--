
import pandas as pd

def recommend_similar(song_title, df_path='clustered_songs.csv', top_n=5):
    """
    Return up to `top_n` songs that are in the same KMeans cluster
    as `song_title`. Assumes `clustered_songs.csv` contains a 'cluster'
    column produced by cluster_songs.py.
    """
    df = pd.read_csv(df_path)

    if song_title not in df['title'].values:
        return f"⚠️ Song '{song_title}' not found."

    cluster_id = df.loc[df['title'] == song_title, 'cluster'].values[0]
    similar = df[(df['cluster'] == cluster_id) & (df['title'] != song_title)]

    return (
        similar[['title', 'artist']]
        .head(top_n)
        .to_dict(orient='records')
    )

if __name__ == '__main__':
    # Quick demo
    for s in recommend_similar('Open Up'):
        print(f"{s['title']} by {s['artist']}")
