import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(page_icon="🌎",page_title="Airbnb", layout="wide")
def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background:url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8SDw0SEw0PEhISDQ0PFRcPDQ8PDxIPFREWFhUSFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKBQUFDgUFDisZExkrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIALEBHAMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAAAAQMCB//EACUQAQACAgEFAAIDAQEAAAAAAAABsTFhcREhQVGBAhKRocEyA//EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwD2yik3GFoCjHBjgoDHC0mODHAKUlLQAUAAdQUQBQAURQAAUTqApAAAAAAAAAAKgCiAMtxjybjCR7hdwC0UbjBuMAUY4N+CgMcLRSY4BaKKKAoKKACgBUUAAFQUARQFQBQARUAUAAAAAAAGO4+wbj7Cbj7Cx7j7ALHuF3GEj3H1dx9Bdxgo3BuAKKNxgoDHBRRQFFFGOAKKMcGOAA6fwoAigigAKgKAAACoAKAAB1AAAOonXQMY9xnzCx7j7CR7jtMZhYjr3jPmAXcfYXcfYc7j7C7j7ALuF3CR7j7Cx7gDcGzp5g3AG/BS7g3AJRjg4woJjhaKKAoojtwUCUtFFABRQCgAIoAAAAKAAgAAAHcO4Ms947TGTPeO0+Tp174mFz3xMAbjPldxnyZ7xldxkEj3H1dwR7jJuMgbhdwR7g4A3BuAA4OA4A4DcG4Aoo3BwBRRwcAUUUY4AVKUAAAEBQAAAASgWUxwUY4An+juY4TpPgEjvqYM6mDOpXOpgDOpg35M8rYG/JZYAWtgIKAIqAGwsDcG4LAODcG4I9wBuCjcG4AgojRsAAFKRQAAEKKAxwY4KOvTgDHCT24McJjgFntwdJ8YTHCfrPiewOs8rnlM8rYGdSWtgFooABIAACKAAgFlhYHT+SyywDcFlgbNwWAbg3BwbgDYbg4AODcG4A2bhNwbgDcYNxg3CdfMYAx3jBjvGKOvmMJjvGPOgOvTv4o/X1PbaY7xjzo/T1PSAacqAFgAAoAAIAAAAioAWAFlgBaWtlgR/ZaWtgWWZ5SwXjJwlrYJuF3BvynGQXcJuDfk3AG4TcfYXcJuP4BNx9hOvmMeYXcfYTcfYBOvTvGPMej9OvePy6Qbj7H+p+kT3j8ugN1AAAEUAAAEVAAAAATQHICKAJYoIWAFmeSywLLLLAssssCzfkzyWBuE3BZuMgm4Nx9g3BuAc7j7H+wfpE94nou4+wn6xPfr04BuAAAAAAAAigIAABICCggAIoAgoCFgBZZZYFlllgZ5M8lpYLaWZ5M8gbjNpuMrZxkE3Dn9Ynv3jh1uMnSJ9g1FAQAAAAAAABFAQAAABFQAUBAAEVADkACwAtLUsEzyZ5CwM8lmeSwJ782naVzynbyDYAAAEAAgUBCAAggAEjAAsYABEAF8JIATgnAATg/JAFnwT4QBZ8JPgAJ8H5eAA/LKflmOABZz8gnIAk/9Of8A0zIA/9k=");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)
setting_bg()
with st.sidebar:
    st.markdown("<h1 style='text-align: center;font-size: 30px;color: red;'>Airbnb Analyis</h1>",
                unsafe_allow_html=True)
    st.image(
        "data:image/jpeg;base64,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")

df = pd.read_csv('extracted_airbnb.csv')
choropleth_data = df[['country', 'Longitude','Latitude']]
fig = px.scatter_geo(choropleth_data, locations="country",
                     hover_name="country",
                     locationmode='country names',
                     projection="natural earth",
                     title="Airbnb Across the World")

st.sidebar.plotly_chart(fig, use_container_width=True)

st.markdown("<h1 style='text-align: center; color: blue'>Airbnb Analysis And Visualization</h1>", unsafe_allow_html=True)
selected = option_menu(None, options=['Home','Location','Analysis'],
                       icons=['house','worldmap','bar_chart'],
                       default_index=0,
                       orientation='horizontal',
                       styles={"nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px",
                                            "--hover-color": "#6495ED"},
                               "icon": {"font-size": "20px"},
                               "container": {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "#93cbf2"}}
                       )

if selected == 'Home':
    c1,c2 = st.columns(2)
    with c1:
        st.write('')
        st.write('')
        st.write('')
        st.image('Airbnb logo.jpg')
    with c2:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.text_area('Airbnb, Inc. is an American company operating an online marketplace for short- and long-term homestays '
                     'and experiences. The company acts as a broker and charges a commission from each booking. '
                     'The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia.')


if selected == 'Location':

   country = st.selectbox('Select Country', df['country'].unique())
   result = df.loc[df['country'] == country, 'property_type'].value_counts().reset_index()
   result.columns = ['property_type', 'count']
   if st.button('DataFrame'):
       st.write(result)
   fig = px.bar(result, x="property_type", y="count", color=result['property_type'], labels={"count": "count"},
                color_continuous_scale='Viridis', title='Number of properties in each country')
   st.plotly_chart(fig, use_container_width=True)
   if st.button('Total Airbnb Listing'):
       listings = df['room_type'].value_counts().reset_index()
       listings.columns = ['room_type','count']
       fig = px.pie(listings, names='room_type', values='count',title='Total Airbnb Listings')
       st.plotly_chart(fig,use_container_width=True)



if selected == 'Analysis':
    analysis_type = st.selectbox('Key feature', ['Price Analysis','Top 5 Properties', 'Room Analysis','Host Analysis'])
    if analysis_type == 'Price Analysis':
        c1,c2 = st.columns(2)
        with c1:
            country = st.selectbox('Select country', df['country'].unique())
            filter_df = df[df['country'] == country]
            avg_price = filter_df.groupby('property_type')['price'].mean().reset_index()
            avg_price.columns = ['property_type','avg_price']
            fig = px.bar(avg_price,'avg_price','property_type',title='price analysis',
                         color_continuous_scale='viridis', color=avg_price['property_type'],orientation='h')
            st.plotly_chart(fig,use_container_width=True)




    if analysis_type == 'Room Analysis':
        c1, c2 = st.columns(2)

        with c1:
            country = st.selectbox('Select country', df['country'].unique())
        filter_df = df[(df['country'] == country)]
        with c2:
            name = st.selectbox('Select property',filter_df['name'])

        filter_df = df[(df['country'] == country) & (df['name'] == name)]
        if st.button('DataFrame'):
            st.write(filter_df.loc[:,['name','bedrooms','beds','room_type','bed_type','price']])


        fig = px.sunburst(filter_df,path = ['room_type','bedrooms','beds','bed_type'],values= 'beds')
        st.plotly_chart(fig)


    if analysis_type =='Top 5 Properties':
        c1,c2 = st.columns(2)
        with c1:
           country = st.selectbox('Select Country',df['country'].unique())
           days = st.slider('select no of days', value = [0,365])
           df['availability_365'] = df['availability_365'].astype(int)
           df['availability_365'].fillna(0,inplace=True)
           filter_df = df[(df['country'] == country) & (df['availability_365'] >= days[1])]
           property_type_counts = filter_df['property_type'].value_counts().reset_index()
           property_type_counts.columns = ['property_type','counts']
           fig = px.bar(property_type_counts.head(),'property_type','counts')
           st.plotly_chart(fig)





    if analysis_type == 'Host Analysis':
        country = st.selectbox('Select Country',df['country'].unique())
        grouped_df = df.groupby(['country', 'host_name'], as_index=False)['host_listings_count'].sum()
        filter_df = grouped_df[grouped_df['country'] == country]
        sorted_df = filter_df.sort_values(by='host_listings_count', ascending=False).head(5)

        fig = px.bar(sorted_df,'host_name','host_listings_count')
        st.plotly_chart(fig,use_container_width=True)
