#helper function - this function is to find all the round trips
import pandas as pd

def find_number_of_round_trips(input_path):

    df_flights = pd.read_csv(input_path)
    round_trip_counts = df_flights.groupby(['ORIGIN','DESTINATION']).size()
    round_trip_counts_df = round_trip_counts.reset_index(name='count')

    #group by trips
    round_trip_counts_df['reverse_count'] = round_trip_counts_df.apply(
        lambda row: round_trip_counts.get((row['DESTINATION'], row['ORIGIN']), 0), axis=1
    )

    # take the min trips between two destinations
    round_trip_counts_df['round_trips'] = round_trip_counts_df[['count', 'reverse_count']].min(axis=1)
    round_trip_counts_df['ROUTE'] = round_trip_counts_df.apply(lambda row: '-'.join([row['ORIGIN'], row['DESTINATION']]), axis=1)
    round_trip_routes = round_trip_counts_df.sort_values(by='round_trips', ascending=False).reset_index(drop = True)
    
    return round_trip_routes