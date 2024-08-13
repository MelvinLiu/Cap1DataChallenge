import pandas as pd
import re
import numpy as np

#need the clean version
tickets_df = pd.read_csv('/Users/yuchengliu/Desktop/c1 data challenge/data_cleaned/cleaned_Tickets.csv')

def check_average_ticket_price(origin, destination):
    route = origin+'-'+destination

    filtered_tickets_df_origin = tickets_df.loc[(tickets_df['ORIGIN'] == origin) & (tickets_df['DESTINATION'] == destination)]
    filtered_tickets_df_destination = tickets_df.loc[(tickets_df['ORIGIN'] == destination) & (tickets_df['DESTINATION'] == origin)]
    
    # check if df is empty
    if not filtered_tickets_df_origin.empty and not filtered_tickets_df_destination.empty:
        filtered_tickets_df = pd.concat([filtered_tickets_df_origin,filtered_tickets_df_destination])
        
    elif filtered_tickets_df_origin.empty and not filtered_tickets_df_destination.empty:
        filtered_tickets_df = filtered_tickets_df_destination
    
    elif not filtered_tickets_df_origin.empty and filtered_tickets_df_destination.empty:
        filtered_tickets_df = filtered_tickets_df_origin
    
    elif filtered_tickets_df_origin.empty and filtered_tickets_df_destination.empty:
        return 0
    
    filtered_tickets_df['ROUTE'] = filtered_tickets_df.apply(lambda row: '-'.join(sorted([row['ORIGIN'], row['DESTINATION']])), axis=1)
    filtered_tickets_df = filtered_tickets_df[['ITIN_ID','ROUTE', 'PASSENGERS', 'ITIN_FARE']]
    
    average_ticket_prices_columns = ['ROUTE', 'TOTAL_PASSENGERS', 'TOTAL_ITIN_FARE', 'AVERAGE_ITIN_FARE']
    average_ticket_prices = pd.DataFrame(columns=average_ticket_prices_columns)
    
    total_passengers = 0
    total_itin_fare = 0

    #for loop to build the number of customer and ticket price
    for index, row in filtered_tickets_df.iterrows():
        route = row['ROUTE']
        passengers = float(row['PASSENGERS'])
        
        if type(row['ITIN_FARE']) == str:
            itin_fare = float(re.sub(r'[^0-9.]', '',row['ITIN_FARE']))
        else:
            itin_fare = row['ITIN_FARE']

        total_passengers += int(passengers)
        total_itin_fare += itin_fare

    #calculate the average price
    avg_ticket_price = total_itin_fare/total_passengers
    if pd.isna(avg_ticket_price):
        return 0
    else:
        return round(avg_ticket_price,2)

#main revenue calculator
def revenue_calculator(occupancy_rate, avg_ticket_price):
    if isinstance(avg_ticket_price, (float, int)) and isinstance(occupancy_rate, (float, int)):
        ticket_sales = occupancy_rate * 200 * avg_ticket_price
        baggage_fees = (occupancy_rate) * 200 * 35
        return ticket_sales + baggage_fees
    else:
        return None