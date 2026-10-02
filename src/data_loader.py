import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', error_bad_lines=False).dropna()
        required_cols= {'Name', 'Genre', 'synopsis'}
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError('Columns are missing')
        df['combined_info'] = (
            f'Title: {df['Name']} Overview: {df['synopsis']} Genres: {df['Genres']}'
        )

        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')
        return self.processed_csv

    