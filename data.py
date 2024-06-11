from pprint import pprint
import json

import pandas as pd

file_path = 'sample_airbnb.json'
with open(file_path, 'r') as json_file:
    data = json.load(json_file)
print(len(data))
df = []
for x in data:
    df1 = {}
    df1['_id'] = x['_id']
    df1['listing_url'] = x.get('listing_url')
    df1['name'] = x.get('name')
    df1['property_type'] = x.get('property_type')
    df1['room_type'] = x.get('room_type')
    df1['bed_type'] = x.get('bed_type')
    df1['minimum_nights'] = x.get('minimum_nights')
    df1['maximum_nights'] = x.get('maximum_nights')
    df1['cancellation_policy'] = x.get('cancellation_policy')
    df1['accommodates'] = x.get('accommodates')
    df1['bedrooms'] = x.get('bedrooms')
    df1['beds'] = x.get('beds')
    df1['number_of_reviews'] = x.get('number_of_reviews')
    df1['bathrooms'] = x.get('bathrooms')
    df1['price'] = x.get('price')
    df1['cleaning_fee'] = x.get('cleaning_fee')
    df1['extra_people'] = x.get('extra_people')
    df1['guests_included'] = x.get('guests_included')
    df1['images'] = x['images'].get('picture_url')
    df1['amenities'] = x.get('amenities')
    df1['review_scores'] = x['review_scores'].get('review_scores_rating',0)
    df.append(df1)
pdf = pd.DataFrame(df)
print(pdf.isnull().sum())
df_host = []
for i in data:
    host_dict = {}
    host_dict['_id'] = i['_id']
    host_dict['host_id'] = i['host']['host_id']
    host_dict['host_url'] = i['host'].get('host_url')
    host_dict['host_name'] = i['host'].get('host_name')
    host_dict['host_location'] = i['host'].get('host_location')
    host_dict['host_about'] = i['host'].get('host_about')
    host_dict['host_response_time'] = i['host'].get('host_response_time')
    host_dict['host_thumbnail_url'] = i['host'].get('host_thumbnail_url')
    host_dict['host_picture_url'] = i['host'].get('host_picture_url')
    host_dict['host_neighbourhood'] = i['host'].get('host_neighbourhood')
    host_dict['host_response_rate'] = i['host'].get('host_response_rate')
    host_dict['host_is_superhost'] = i['host'].get('host_is_superhost')
    host_dict['host_has_profile_pic'] = i['host'].get('host_has_profile_pic')
    host_dict['host_identity_verified'] = i['host'].get('host_identity_verified')
    host_dict['host_listings_count'] = i['host'].get('host_listings_count')
    host_dict['host_total_listings_count'] = i['host'].get('host_total_listings_count')
    host_dict['host_verifications'] = i['host'].get('host_verifications')
    df_host.append(host_dict)
pdf_host = pd.DataFrame(df_host)
print(pdf_host)
df_address = []
for i in data:
    address_dict = {}
    address_dict['_id'] = i['_id']
    address_dict['street'] = i['address'].get('street')
    address_dict['suburb'] = i['address'].get('suburb')
    address_dict['government_area'] = i['address'].get('government_area')
    address_dict['market'] = i['address'].get('market')
    address_dict['country'] = i['address'].get('country')
    address_dict['country_code'] = i['address'].get('country_code')
    address_dict['type'] = i['address']['location'].get('type')
    address_dict['Longitude'] = i['address']['location'].get('coordinates')[0]
    address_dict['Latitude'] = i['address']['location'].get('coordinates')[1]
    address_dict['is_location_exact'] = i['address']['location'].get('is_location_exact')
    df_address.append(address_dict)
pdf_address = pd.DataFrame(df_address)

df_availability = []
for i in data:
    availability_dict = {}
    availability_dict['_id'] = i['_id']
    availability_dict['availability_30'] = i['availability'].get('availability_30')
    availability_dict['availability_60'] = i['availability'].get('availability_60')
    availability_dict['availability_90'] = i['availability'].get('availability_90')
    availability_dict['availability_365'] = i['availability'].get('availability_365')
    df_availability.append(availability_dict)
pdf_availability = pd.DataFrame(df_availability)
merge_df = pd.merge(pdf,pdf_host , on ='_id')
merge_df1 = pd.merge(merge_df,pdf_address, on='_id')
merge_df2 = pd.merge(merge_df1, pdf_availability, on='_id')
merge_df2['bedrooms'].fillna(0,inplace= True)
merge_df2['beds'].fillna(0,inplace= True)
merge_df2['bathrooms'].fillna(0,inplace= True)
merge_df2['cleaning_fee'].fillna('0',inplace= True)
merge_df2['cleaning_fee'] = merge_df2['cleaning_fee'].astype(float)
merge_df2['host_response_time'].fillna('Not Specified',inplace=True)
merge_df2['host_response_rate'].fillna('Not Specified',inplace=True)
merge_df2['host_is_superhost'] = merge_df2['host_is_superhost'].map({False: 'No', True: 'Yes'})
merge_df2['host_has_profile_pic'] = merge_df2['host_has_profile_pic'].map({False: 'No', True: 'Yes'})
merge_df2['host_identity_verified'] = merge_df2['host_identity_verified'].map({False: 'No', True: 'Yes'})
merge_df2['minimum_nights'] = merge_df2['minimum_nights'].astype(int)
merge_df2['maximum_nights'] = merge_df2['maximum_nights'].astype(int)
merge_df2['bedrooms'] = merge_df2['bedrooms'].astype(int)
merge_df2['beds'] = merge_df2['beds'].astype(int)
merge_df2['bathrooms'] = merge_df2['bathrooms'].astype(float)
merge_df2['price'] = merge_df2['price'].astype(float)
merge_df2['availability_365'].astype(int)

print(pdf.isnull().sum())

print(merge_df2.dtypes)
merge_df2.to_csv('extracted_airbnb.csv', index=False)

print(merge_df2)
print(merge_df2.isnull().sum())








