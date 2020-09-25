from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px

router = APIRouter()


@router.get('/viz/{location}')
async def viz(location: str):
    """
    ## Visualize locations for users to check their airbnb optimal price rates
    
    ### Path Parameter
    `location`: The [USPS 2 letter abbreviation](https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations#Table)
    (https://www.britannica.com/topic/list-of-countries-1993160) 
    (case insensitive) for any of the 50 locations or the District of Columbia.

    ### Response
    JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
    """
    
    # Validate the location
    locations = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 
        'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 
        'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida', 
        'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 
        'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 
        'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 
        'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 
        'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 
        'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 
        'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 
        'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 
        'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 
        'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 
        'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 
        'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 
        'WI': 'Wisconsin', 'WY': 'Wyoming'
    }
    

    # Get the location's locations for users to check the optimal price rate
    url = "https://raw.githubusercontent.com/fallenleaves404/NYC_Airbnb_Analysis/master/AB_NYC_2019.csv"
    df1 = pd.read_csv(url)

    # We can improve the location much better by making a scatter mapbox
    # https://plot.ly/python/mapbox-layers/#base-maps-in-layoutmapboxstyle
    fig = px.scatter_mapbox(df1, lat='latitude', lon='longitude', color='price', opacity=0.1)
    fig.update_layout(mapbox_style='stamen-terrain')

    # Return Plotly figure as JSON string
    return fig.to_json()
