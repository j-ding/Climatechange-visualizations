#!/usr/bin/env python
# coding: utf-8

# In[4]:


import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='jding156', api_key='xjMXkUH5eDSOjbYpDIz1')
import pandas as pd
df = pd.read_csv (r'co2.csv')
y1=df['1960']
y2=df['1970']
y3=df['1980']
y4=df['1990']
y5=df['2000']
y6=df['2010']
y7=df['1965']
y8=df['1975']
y9=df['1985']
y10=df['1995']
y11=df['2005']
y12=df['2015']

p1 = go.Box(
y=y1,
name='1960'
)

p2 = go.Box(
y=y2,
name='1970'
)

p3 = go.Box(
y=y3,
name= '1980'
)

p4 = go.Box(
y=y4,
name= '1990'
)

p5 = go.Box(
y=y5,
name= '2000'
)

p6 = go.Box(
y=y6,
name= '2010'
)

p7 = go.Box(
y=y7,
name= '1965'
)

p8 = go.Box(
y=y8,
name= '1975'
)

p9 = go.Box(
y=y9,
name= '1985'
)

p10 = go.Box(
y=y10,
name= '1995'
)

p11 = go.Box(
y=y11,
name= '2005'
)

p12 = go.Box(
y=y12,
name= '2015'
)



data = [p1, p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
py.iplot(data)


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("GlobalTemps.csv")
data["dt"] = pd.to_datetime(data["dt"])
mean_global = data.groupby(data["dt"].dt.year).mean()
temperature_global = mean_global.loc[1850:2015].mean()["LandAndOceanAverageTemperature"]
mean_global["Anomaly"] = mean_global["LandAndOceanAverageTemperature"] - temperature_global

plt.figure()
plt.style.use("bmh")
mean_global.loc[1850:2015]["Anomaly"].plot(figsize = (15,8))
plt.title("Average Δ Temperature Annually (Global)")
plt.xlabel('Year')
plt.ylabel('Temperature Increase °C')
plt.show()


# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import time

global_temp_country = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
global_temp = pd.read_csv("GlobalTemps.csv")


years = np.unique(global_temp['dt'].apply(lambda x: x[:4]))

continent = ['China', 'United States', 'Mexico', 'Japan', 'Australia', 'Russia']

mean_temp_year_country = [ [0] * len(years[70:]) for i in range(len(continent))]
j = 0

global_temp_country_clear = global_temp_country[~global_temp_country['Country'].isin(
    ['Denmark','South America'])]


for country in continent:
    all_temp_country = global_temp_country_clear[global_temp_country_clear['Country'] == country]
    i = 0
    for year in years[70:]:
        mean_temp_year_country[j][i] = all_temp_country[all_temp_country['dt'].apply(
                lambda x: x[:4]) == year]['AverageTemperature'].mean()
        i +=1
    j += 1

traces = []
colors = ['rgb(127, 0, 255)','rgb(0, 255, 255)', 'rgb(0, 0, 255)', 'rgb(0, 255, 0)',
          'rgb(255, 0, 0)', 'rgb(0, 0, 0)']
for i in range(len(continent)):
    traces.append(go.Scatter(
        x=years[60:],
        y=mean_temp_year_country[i],
        mode='lines',
        name=continent[i],
        line=dict(color=colors[i]),
    ))

layout = go.Layout(
    xaxis=dict(title='Year'),
    yaxis=dict(title='Average Temperature - °C'),
    title='Average Temperature Increase by Continents',)

fig = go.Figure(data=traces, layout=layout)
py.iplot(fig)


# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go


global_temp = pd.read_csv("GlobalTemps.csv")

#Extract the year from a date
years = np.unique(global_temp['dt'].apply(lambda x: x[:4]))
mean_temp_world = []
mean_temp_world_uncertainty = []

for year in years:
    mean_temp_world.append(global_temp[global_temp['dt'].apply(
        lambda x: x[:4]) == year]['LandAverageTemperature'].mean())
    mean_temp_world_uncertainty.append(global_temp[global_temp['dt'].apply(
                lambda x: x[:4]) == year]['LandAverageTemperatureUncertainty'].mean())

trace0 = go.Scatter(
    x = years, 
    y = np.array(mean_temp_world) + np.array(mean_temp_world_uncertainty),
    fill= None,
    mode='lines',
    name='Uncertainty pos',
    line=dict(
        color='rgb(199, 0, 0)',
    )
)
trace1 = go.Scatter(
    x = years, 
    y = np.array(mean_temp_world) - np.array(mean_temp_world_uncertainty),
    fill='tonexty',
    mode='lines',
    name='Uncertainty neg',
    line=dict(
        color='rgb(199, 0, 0)',
    )
)

trace2 = go.Scatter(
    x = years, 
    y = mean_temp_world,
    mode='lines',
    name='Average Temperature',
    line=dict(
        color='rgb(0, 0, 0)',
    )
)
data = [trace0, trace1, trace2]

layout = go.Layout(
    xaxis=dict(title='Year'),
    yaxis=dict(title='Average Temperature - °C'),
    title='Average World Temperature ',
    showlegend = False)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[9]:


import sqlite3
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import pandas as pd

conn = sqlite3.connect("FPA_FOD_20170508.sqlite")
df = pd.read_sql_query("SELECT FIRE_YEAR,LATITUDE,LONGITUDE,FIRE_SIZE from Fires                        WHERE FIRE_SIZE_CLASS='G';",conn)
data = []
layout = dict(
    title = 'US Wildfires 1992 to 2015' ,
    showlegend = False,
    autosize = False,
    width = 1100,
    height = 1000,
    hovermode = False,
    legend = dict(
        x=0.1,
        y=-0.1,
        bgcolor="rgba(175, 170, 150, 0)",
        font = dict( size= 1 ),
    )
)
years = sorted(df['FIRE_YEAR'].unique())

for i in range(len(years)):
    geo_key = 'geo'+str(i+1) if i != 0 else 'geo'
    lons = list(df[ df['FIRE_YEAR'] == years[i] ]['LONGITUDE'])
    lats = list(df[ df['FIRE_YEAR'] == years[i] ]['LATITUDE'])
    data.append(
        dict(
            type = 'scattergeo',
            showlegend=False,
            lon = lons,
            lat = lats,
            geo = geo_key,
            name = str(years[i]),
            marker = dict(
                color = "rgb(255, 120, 0)",
                opacity = 0.5
            )
        )
    )
    data.append(
        dict(
            type = 'scattergeo',
            showlegend = False,
            lon = [-78],
            lat = [47],
            geo = geo_key,
            text = [years[i]],
            mode = 'text',
        )
    )
    
    layout[geo_key] = dict(
        scope = 'usa',
        showland = True,
        landcolor = 'rgb(229, 229, 229)',
        showcountries = False,
        domain = dict( x = [], y = [] ),
        subunitcolor = "rgb(255, 255, 255)",
    )
    
z = 0
COLS = 4
ROWS = 6

for y in reversed(range(ROWS)):
    for x in range(COLS):
        geo_key = 'geo'+str(z+1) if z != 0 else 'geo'
        layout[geo_key]['domain']['x'] = [float(x)/float(COLS), float(x+1)/float(COLS)]
        layout[geo_key]['domain']['y'] = [float(y)/float(ROWS), float(y+1)/float(ROWS)]
        z=z+1

fig = dict(data=data, layout=layout)
config = {'scrollZoom': False}
iplot( fig, filename='US Wildfires 1992 to 2015', config=config)


# In[10]:


from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from PIL import Image  
import numpy as np

def plotly_wordcloud(text):
    wc = WordCloud(stopwords = set(STOPWORDS),
                   max_words = 9999999,
                   max_font_size = 50)
    wc.generate(text)
    
    word_list=[]
    freq_list=[]
    fontsize_list=[]
    position_list=[]
    orientation_list=[]
    color_list=[]

    for (word, freq), fontsize, position, orientation, color in wc.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)
        
    # get the positions
    x=[]
    y=[]
    for i in position_list:
        x.append(i[0])
        y.append(i[1])
            
    # get the relative occurence frequencies
    new_freq_list = []
    for i in freq_list:
        new_freq_list.append(i*100)
    new_freq_list
    
    trace = go.Scatter(x=x, 
                       y=y, 
                       textfont = dict(size=new_freq_list,
                                       color=color_list),
                       hoverinfo='text',
                       hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)],
                       mode="text",  
                       text=word_list
                      )
    
    layout = go.Layout(
                       xaxis=dict(showgrid=False, 
                                  showticklabels=False,
                                  zeroline=False,
                                  automargin=True),
                       yaxis=dict(showgrid=False,
                                  showticklabels=False,
                                  zeroline=False,
                                  automargin=True)
                      )
    
    fig = go.Figure(data=[trace], layout=layout)
    
    return fig

text=("Global warming is a long-term rise in the average temperature of the Earth's climate system; an aspect of climate change shown by temperature measurements and by multiple effects of the warming.[2][3] Though earlier geological periods also experienced episodes of warming,[4] the term commonly refers to the observed and continuing increase in average air and ocean temperatures since 1900 caused mainly by emissions of greenhouse gases (GHGs) in the modern industrial economy.[5] In the modern context the terms global warming and climate change are commonly used interchangeably,[6] but climate change includes both global warming and its effects, such as changes to precipitation and impacts that differ by region.[7] Many of the observed changes in climate since the 1950s are unprecedented in the instrumental temperature record, and in historical and paleoclimate proxy records of climate change over thousands to millions of years.[8] In 2013, the Intergovernmental Panel on Climate Change (IPCC) Fifth Assessment Report concluded, It is extremely likely that human influence has been the dominant cause of the observed warming since the mid-20th century.[9] The largest human influence has been the emission of greenhouse gases such as carbon dioxide, methane, and nitrous oxide. Climate model projections summarized in the report indicated that during the 21st century, the global surface temperature is likely to rise a further 0.3 to 1.7 °C (0.5 to 3.1 °F) in a moderate scenario, or as much as 2.6 to 4.8 °C (4.7 to 8.6 °F) in an extreme scenario, depending on the rate of future greenhouse gas emissions and on climate feedback effects.[10] These findings have been recognized by the national science academies of the major industrialized nations[11][a] and are not disputed by any scientific body of national or international standing.[13][14] Effects of global warming include rising sea levels, regional changes in precipitation, more frequent extreme weather events such as heat waves, and expansion of deserts.[15] Surface temperature increases are greatest in the Arctic, with the continuing retreat of glaciers, permafrost, and sea ice. Overall, higher temperatures bring more rain and snowfall, but for some regions droughts and wildfires increase instead.[16] Climate change impacts humans by, amongst other things, threatening food security from decreasing crop yields, and the abandonment of populated areas and damage to infrastructure due to rising sea levels.[17][18] Environmental impacts include the extinction or relocation of ecosystems as they adapt to climate change, with coral reefs,[19] mountain ecosystems, and Arctic ecosystems most immediately threatened.[20] Because the climate system has a large inertia and greenhouse gases will remain in the atmosphere for a long time, climatic changes and their effects will continue to become more pronounced for many centuries even if further increases to greenhouse gases stop.[21] Globally, a majority of people consider global warming a serious or very serious issue.[22] Possible societal responses to global warming include mitigation by emissions reduction, adaptation to its effects, and possible future climate engineering. Every country in the world is a party to the United Nations Framework Convention on Climate Change (UNFCCC),[23] whose ultimate objective is to prevent dangerous anthropogenic climate change.[24] Parties to the UNFCCC have agreed that deep cuts in emissions are required[25] and that global warming should be limited to well below 2 °C (3.6 °F) compared to pre-industrial levels,{{efn|Earth has already experienced almost 1/2 of the 2.0 °C (3.6 °F) described in the Cancún Agreement. In the last 100 years, Earth's average surface temperature increased by about 0.8 °C (1.4 °F) with about two-thirds of the increase occurring over just the last three decades. [26] with efforts made to limit warming to 1.5 °C (2.7 °F).[27] Some scientists call into question climate adaptation feasibility, with higher emissions scenarios,[28] or the two degree temperature target.[29] Contents Observed temperature changes Main article: Instrumental temperature record Annual (thin lines) and five-year lowess smooth (thick lines) for the temperature anomalies averaged over the Earth's land area (red line) and sea surface temperature anomalies (blue line) averaged over the part of the ocean that is free of ice at all times (open ocean). Two millennia of mean surface temperatures according to different reconstructions from climate proxies, each smoothed on a decadal scale, with the instrumental temperature record overlaid in black. Multiple independently produced datasets confirm that between 1880 and 2012, the global average (land and ocean) surface temperature increased by 0.85 [0.65 to 1.06] °C.[30] Currently, surface temperature rise with about 0.2 °C degrees per decade.[31] Since 1950, the number of cold days and nights have decreased, and the number of warm days and night have increased.[32] These trends can be compared to historical temperature trends: patterns of warming and cooling like the Medieval Climate Anomaly and the Little Ice Age were not as synchronous as current warming, but did reach temperatures as high as late-20th century regionally.[33] Although the increase of the average near-surface atmospheric temperature is commonly used to track global warming, over 90% of the additional energy stored in the climate system over the last 50 years is in warmer ocean water.[34] The rest has melted ice and warmed the continents and the atmosphere.[35] Melting ice (including Arctic sea ice, ice sheets and glaciers) and warming of the continents and atmosphere account for the remainder of the change in energy. The warming evident in the instrumental temperature record is consistent with a wide range of observations, documented by many independent scientific groups,[36] for example in most continental regions the frequency and intensity of heavy precipitation has increased.[37] Further examples include sea level rise,[38] widespread melting of snow and land ice,[39] increased heat content of the oceans,[36] increased humidity,[36] and the earlier timing of spring events,[40] such as the flowering of plants.[41] Regional trends See also: Regional effects of global warming and Polar amplification Global warming refers to global averages, with the amount of warming varying by region. Since 1979, global average land temperatures have increased about twice as fast as global average ocean temperatures.[42][needs update?] This is due to the larger heat capacity of the oceans and because oceans lose more heat by evaporation.[43] Where greenhouse gas emissions occur does not impact the location of warming because the major greenhouse gases persist long enough to diffuse across the planet, although localized black carbon deposits on snow and ice do contribute to Arctic warming.[44] The Northern Hemisphere and North Pole have heated much faster than the South Pole and Southern Hemisphere. The Northern Hemisphere not only has much more land, its arrangement around the Arctic Ocean has resulted in the maximum surface area flipping from reflective snow and ice cover to ocean and land surfaces that absorb more sunlight.[45] Arctic temperatures have increased and are predicted to continue to increase during this century at over twice the rate of the rest of the world.[46][needs update?] As the temperature difference between the Arctic and the equator decreases ocean currents that are driven by that temperature difference, like the Gulf Stream, are weakening.[47] Short-term slowdowns and surges Because the climate system has large thermal inertia, it can take centuries for the climate to fully adjust. While record-breaking years attract considerable public interest, individual years are less significant than the overall trend. Global surface temperature is subject to short-term fluctuations that overlay long-term trends, and can temporarily mask or magnify them.[48] An example of such an episode is the slower rate of surface temperature increase from 1998 to 2012, which was dubbed the global warming hiatus by the media and some scientists.[49] Throughout this period ocean heat storage continued to progress steadily upwards, and in subsequent years surface temperatures have spiked upwards. The slower pace of warming can be attributed to heating and cooling in the Pacific Ocean from natural variability such as El Niño and La Nina events, reduced solar activity, and a number of volcanic eruptions that inserted sunlight-reflecting particles into the atmosphere.[50] Physical drivers of climate change Refer to caption Contribution of natural factors and human activities to radiative forcing of climate change.[51] Radiative forcing values are for the year 2005, relative to the pre-industrial era (1750).[51] The contribution of solar irradiance to radiative forcing is 5% of the value of the combined radiative forcing due to increases in the atmospheric concentrations of carbon dioxide, methane and nitrous oxide.[52] Further information: Attribution of recent climate change By itself, the climate system may generate changes in global temperatures for years (such as the El Niño–Southern Oscillation) to decades[53] or centuries[54] at a time. Other changes emanate from so-called external forcings. These forcings are external to the climate system, but not necessarily external to Earth.[55] Examples of external forcings include changes in the composition of the atmosphere (e.g., increased concentrations of greenhouse gases), solar luminosity, volcanic eruptions, and variations in Earth's orbit around the Sun.[56] Attributing detected temperature changes and extreme events to man-made increases in greenhouse gases requires scientists to rule out known internal climate variability and natural external forcings. So a key approach is to use physical models of the climate system to determine unique fingerprints for all potential external forcings. By comparing these fingerprints with the observed pattern and evolution of the climate change, and the observed evolution of the forcings, the causes of the observed changes can be determined.[57] Greenhouse gases Greenhouse effect schematic showing energy flows between space, the atmosphere, and Earth's surface. Energy exchanges are expressed in watts per square meter (W/m2). CO 2 concentrations over the last 800,000 years as measured from ice cores (blue/green) and directly (black). Main articles: Greenhouse gas, Greenhouse effect, and Carbon dioxide in Earth's atmosphere Greenhouse gases trap heat radiating from Earth to space.[58] This heat, in the form of infrared radiation, gets absorbed and emitted by these gases in the planet's atmosphere thus warming the lower atmosphere and the surface. On Earth, an atmosphere containing naturally occurring amounts of greenhouse gases causes air temperature near the surface to be warmer by about 33 °C (59 °F) than it would be in their absence.[59][b] Without the Earth's atmosphere, the Earth's average temperature would be well below the freezing temperature of water.[60] The major greenhouse gases are water vapour, which causes about 36–70% of the greenhouse effect; carbon dioxide (CO2), which causes 9–26%; methane (CH4), which causes 4–9%; and ozone (O3), which causes 3–7%.[61][62][63] Human activity since the Industrial Revolution has increased the amount of greenhouse gases in the atmosphere, leading to increased radiative forcing from CO2, methane, tropospheric ozone, CFCs, and nitrous oxide. In 2011, the concentrations of CO2 and methane had increased by about 40% and 150% respectively since pre-industrial times,[64] with CO2 readings taken at the world's primary benchmark site in Mauna Loa surpassing 400 ppm in 2013 for the first time.[65] These levels are much higher than at any time during the last 800,000 years, the period for which reliable data has been extracted from ice cores.[66] Less direct geological evidence indicates that CO2 values haven't been this high for millions of years.[65] Global anthropogenic greenhouse gas emissions in 2010 were 49 billion tonnes of carbon dioxide-equivalents per year (using the most recent global warming potentials over 100 years from the AR5 report). Of these emissions, 65% was carbon dioxide from fossil fuel burning and industry, 11% was carbon dioxide from land use change, which is primarily due to deforestation, 16% was methane, 6.2% was nitrous oxide, and 2.0% were fluorinated gases.[67] Using life-cycle assessment to estimate emissions relating to final consumption, the dominant sources of 2010 emissions were: food (26–30% of emissions);[68] washing, heating and lighting (26%); personal transport and freight (20%); and building construction (15%).[69] Land use change Changing the type of vegetation in a region impacts the local temperature by changing how much sunlight gets reflected back into space and how much heat is lost by evaporation. For instance, the change from a dark forest to grassland makes the surface lighter, and causes it to reflect more sunlight: an increase in albedo. Humans change the land surface mainly to create more agricultural land.[70] Since the pre-industrial era, albedo increased due to land use change, which has a cooling effect on the planet. Other processes linked to land use change however have had the opposite effect, so that the net effect remains unclear.[71] Aerosols and soot Refer to caption Ship tracks can be seen as lines in these clouds over the Atlantic Ocean on the East Coast of the United States, an example of the Twomey effect. Solid and liquid particles known as aerosols – from volcanoes, plankton and human-made pollutants – reflect incoming sunlight,[72] cooling the climate.[73] From 1961 to 1990, a gradual reduction in the amount of sunlight reaching the Earth's surface was observed, a phenomenon popularly known as global dimming,[74] typically attributed to aerosols from biofuel and fossil fuel burning.[75] Aerosol removal by precipitation gives tropospheric aerosols an atmospheric lifetime of only about a week, while stratospheric aerosols can remain in the atmosphere for a few years.[76] Global aerosols have been declining since 1990, removing some of the masking of global warming that aerosols had been providing.[77] In addition to their direct effect by scattering and absorbing solar radiation, aerosols have indirect effects on the Earth's radiation budget. Sulfate aerosols act as cloud condensation nuclei and thus lead to clouds that have more and smaller cloud droplets. These clouds reflect solar radiation more efficiently than clouds with fewer and larger droplets, a phenomenon known as the Twomey effect.[78] This effect also causes droplets to be of more uniform size, which reduces growth of raindrops and makes the cloud more reflective to incoming sunlight, known as the Albrecht effect.[79] Indirect effects of aerosols are the largest uncertainty in radiative forcing.[80][needs update] While aerosols typically limit global warming by reflecting sunlight, if black carbon in soot falls on snow or ice, it can also increase global warming. Not only does it increase the absorption of sunlight, it also increases melting and sea level rise.[81] Limiting new black carbon deposits in the Arctic could reduce global warming by 0.2 degrees Celsius by 2050.[82] When soot is suspended in the atmosphere, it directly absorbs solar radiation, heating the atmosphere and cooling the surface. In areas with high soot production, such as rural India, as much as 50% of surface warming due to greenhouse gases may be masked by atmospheric brown clouds.[83] The influences of atmospheric particles, including black carbon, are most pronounced in the tropics and northern mid-latitudes, with the effects of greenhouse gases dominant in the other parts of the world.[84][85] Incoming sunlight Further information: Solar activity and climate As the Sun is Earth's primary energy source, changes in incoming sunlight directly affect the climate system.[86] Solar irradiance has been measured directly by satellites since 1978,[87] but indirect measurements are available beginning in the early 1600s.[86] There has been no upward trend in the amount of the Sun's energy reaching the Earth, so it cannot be responsible for the current warming.[88] Physical climate models are also unable to reproduce the rapid warming observed in recent decades when taking into account only variations in solar output and volcanic activity.[89] Another line of evidence for the warming not being due to the Sun is the temperature changes at different levels in the Earth's atmosphere.[90] According to basic physical principles, the greenhouse effect produces warming of the lower atmosphere (the troposphere), but cooling of the upper atmosphere (the stratosphere).[91] If solar variations were responsible for the observed warming, warming of both the troposphere and the stratosphere would be expected, but that has not been the case.[92] While variations in solar activity have not produced recent global warming, variations in solar output over geologic time (millions to billions of years ago) are believed to have caused major changes in the earth's climate.[93][failed verification] The 11-year solar cycle of sunspot activity also introduces climate changes that have a small cyclical effect on annual global temperatures.[94] The tilt of the Earth's axis and the shape of its orbit around the Sun vary slowly over tens of thousands of years in a phenomenon known as the Milankovitch cycles. This changes climate by changing the seasonal and latitudinal distribution of incoming solar energy at the Earth's surface,[95] resulting in periodic glacial and interglacial periods over the last few million years.[96] During the last few thousand years, this phenomenon contributed to a slow cooling trend at high latitudes of the Northern Hemisphere during summer, a trend that was reversed by greenhouse-gas-induced warming during the 20th century.[97] Orbital cycles favourable for glaciation are not expected within the next 50,000 years.[98] Climate change feedback Main articles: Climate change feedback and Climate sensitivity The dark ocean surface reflects only 6 percent of incoming solar radiation, whereas sea ice reflects 50 to 70 percent.[99] The response of the climate system to an initial forcing is increased by positive feedbacks and reduced by negative feedbacks.[100] The main negative feedback to global temperature change is radiative cooling to space as infrared radiation, which increases strongly with increasing temperature.[101] The main positive feedbacks are the water vapour feedback, the ice–albedo feedback, and probably the net effect of clouds.[102] Uncertainty over feedbacks is the major reason why different climate models project different magnitudes of warming for a given amount of emissions.[103] As air gets warmer, it can hold more moisture. After an initial warming due to emissions of greenhouse gases, the atmosphere will hold more water. As water is a potent greenhouse gas, this further heats the climate: the water vapour feedback.[102] The reduction of snow cover and sea ice in the Arctic reduces the albedo (reflectivity) of the Earth's surface.[104] More of the sun's energy is now absorbed in these regions, contributing to Arctic amplification, which has caused Arctic temperatures to increase at almost twice the rate of the rest of the world.[46] Arctic amplification also causes methane to be released as permafrost melts, which is expected to surpass land use changes as the second strongest anthropogenic source of greenhouse gases by the end of the century.[105] Cloud cover may change in the future. To date, cloud changes have had a cooling effect, with NASA estimating that aerosols produced by the burning of hydrocarbons have limited warming by half from 1850 to 2010.[72] An analysis of satellite data between 1983 and 2009 reveals that cloud tops are reaching higher into the atmosphere and that cloudy storm tracks are shifting toward Earth's poles, suggesting clouds will be a positive feedback in the future.[106] Carbon dioxide stimulates plant growth so the carbon cycle has been a negative feedback so far: roughly half of each year's CO2 emissions have been absorbed by plants on land and in oceans,[107] with an estimated 30% increase in plant growth from 2000 to 2017.[108] The limits and reversal point for this feedback are an area of uncertainty.[109] As more CO2 and heat are absorbed by the ocean it is acidifying and ocean circulation can change, changing the rate at which the ocean can absorb atmospheric carbon.[110] On land, greater plant growth will be constrained by nitrogen levels and can be reversed by plant heat stress, desertification, and the release of carbon from soil as the ground warms.[111] A concern is that positive feedbacks will lead to a tipping point, where global temperatures transition to a hothouse climate state even if greenhouse gas emissions are reduced or eliminated. A 2018 study tried to identify such a planetary threshold for self-reinforcing feedbacks and found that even a 2 °C (3.6 °F) increase in temperature over pre-industrial levels, may be enough to trigger such a hothouse Earth scenario.[112] Climate models Future CO2 projections, including all forcing agents' atmospheric CO2-equivalent concentrations (in parts-per-million-by-volume (ppmv)) according to four RCPs (Representative Concentration Pathways). Projected change in annual mean surface air temperature from the late 20th century to the middle 21st century, based on a medium emissions scenario.[113] This scenario assumes that no future policies are adopted to limit greenhouse gas emissions. Image credit: NOAA GFDL.[114] Main article: Global climate model A climate model is a representation of the physical, chemical and biological processes that affect the climate system.[115] Computer models are run on supercomputers to reproduce and predict the circulation of the oceans, the annual cycle of the seasons, and the flows of carbon between the land surface and the atmosphere.[116] There are more than two dozen scientific institutions that develop climate models.[116] Model forecasts vary due to different greenhouse gas inputs and different assumptions about the impact of different feedbacks on climate sensitivity. A subset of climate models add societal factors to a simple physical climate model. These models simulate how population, economic growth and energy use affect – and interact with – the physical climate. With this information, scientists can produce scenarios of how greenhouse gas emissions may vary in the future. Scientists can then run these scenarios through physical climate models to generate climate change projection.[116] Climate models include different external forcings for their models. For different greenhouse gas inputs four RCPs (Representative Concentration Pathways) are used: a stringent mitigation scenario (RCP2.6), two intermediate scenarios (RCP4.5 and RCP6.0) and one scenario with very high GHG emissions (RCP8.5).[117] Models also include changes in the Earth's orbit, historical changes in the sun's activity and volcanic forcing.[116] RCPs only look at concentrations of greenhouse gases, factoring out uncertainty as to whether the carbon cycle will continue to remove about half of the carbon dioxide from the atmosphere each year.[118] The physical realism of models is tested by examining their ability to simulate contemporary or past climates.[119] Past models have underestimated the rate of Arctic shrinkage[120] and underestimated the rate of precipitation increase.[121] Sea level rise since 1990 was underestimated in older models, but now agrees well with observations.[122] The 2017 United States-published National Climate Assessment notes that climate models may still be underestimating or missing relevant feedback processes.[123] Effects Main article: Effects of global warming Historical sea level reconstruction and projections up to 2100 published in January 2017 by the U.S. Global Change Research Program for the Fourth National Climate Assessment.[124] Map of the Earth with a six-meter sea level rise represented in red. Physical environmental Main article: Physical impacts of climate change The environmental effects of global warming are broad and far-reaching. They include the following diverse effects: Arctic sea ice decline, sea level rise, retreat of glaciers: global warming has led to decades of shrinking and thinning of the Arctic sea ice, making it vulnerable to atmospheric anomalies.[125] Projections of declines in Arctic sea ice vary.[126] Recent projections suggest that Arctic summers could be ice-free (defined as an ice extent of less than 1 million square km) as early as 2025–2030.[127] Since 1993, sea level has on average risen with 3.1 ± 0.3 mm per year. Additionally, sea level rise has accelerated from 1993 to 2017.[128] Over the 21st century, the IPCC projects (for a high emissions scenario) that global mean sea level could rise by 52–98 cm.[129] The rate of ice loss from glaciers and ice sheets in the Antarctic is a key area of uncertainty since Antarctica contains 90% of potential sea level rise.[130] Polar amplification and increased ocean warmth are undermining and threatening to unplug Antarctic glacier outlets, potentially resulting in more rapid sea level rise.[131] Extreme weather, extreme events, tropical cyclones: Globally, many regions have probably already seen increases in warm spells and heat waves and it's virtually certain these changes continue over the 21st century.[132] Data analysis of extreme events from 1960 until 2010 suggests that droughts and heat waves appear simultaneously with increased frequency.[133][better source needed] Extremely wet or dry events within the monsoon period have increased since 1980.[134][better source needed] Studies have also linked the rapidly warming Arctic to extreme weather in mid-latitudes as the jet stream becomes more erratic.[135][additional citation(s) needed] Maximum rainfall and wind speed from hurricanes and typhoons are likely increasing.[136] Changes in ocean properties: increases in atmospheric CO2 concentrations have led to an increase in dissolved CO2 and as a consequence ocean acidity.[137] Furthermore, oxygen levels decrease because oxygen is less soluble in warmer water, an effect known as ocean deoxygenation.[138] Long-term effects of global warming: On the timescale of centuries to millennia, the magnitude of global warming will be determined primarily by anthropogenic CO2 emissions.[139] This is due to carbon dioxide's very long lifetime in the atmosphere.[139] Long-term effects also include a response from the Earth's crust, due to ice melting and deglaciation, in a process called post-glacial rebound, when land masses are no longer depressed by the weight of ice. This could lead to landslides and increased seismic and volcanic activities. Tsunamis could be generated by submarine landslides caused by warmer ocean water thawing ocean-floor permafrost or releasing gas hydrates.[140] Sea level rise will continue over many centuries.[141] Abrupt climate change, tipping points in the climate system: Climate change could result in global, large-scale changes.[142] Some large-scale changes could occur abruptly, i.e. over a short time period, and might also be irreversible. Examples of abrupt climate change are the rapid release of methane and carbon dioxide from permafrost, which would lead to amplified global warming. Another example is the possibility for the Atlantic Meridional Overturning Circulation to slow or to shut down (see also shutdown of thermohaline circulation).[143][144] This could trigger cooling in the North Atlantic, Europe, and North America.[145] Biosphere As the climate change melts sea ice, the U.S. Geological Survey projects that two-thirds of polar bears will disappear by 2050.[146] Main article: Climate change and ecosystems Ecosystem changes: In terrestrial ecosystems, the earlier timing of spring events, as well as poleward and upward shifts in plant and animal ranges, have been linked with high confidence to recent warming.[147] It is expected that most ecosystems will be affected by higher atmospheric CO2 levels, combined with higher global temperatures.[148] Expansion of deserts in the subtropics is probably linked to global warming.[149][needs update?] Ocean acidification threatens damage to coral reefs, fisheries, protected species, and other natural resources of value to society.[137][150] Without substantial actions to reduce the rate of global warming, land-based ecosystems are at risk of major ecological shifts, transforming composition and structure.[151] Overall, it is expected that climate change will result in the extinction of many species and reduced diversity of ecosystems.[152] Rising temperatures have been found to push bees to their physiological limits, and could cause the extinction of bee populations.[153] Continued ocean uptake of CO2 may affect the brains and central nervous system of certain fish species, and that this impacts their ability to hear, smell, and evade predators.[154] Impacts on humans Further information: Effects of global warming on human health, Climate security, Economics of global warming, and Climate change and agriculture A helicopter drops water on a wildfire in California. Drought and higher temperatures linked to climate change are driving a trend towards larger fires.[155] The effects of climate change on human systems, mostly due to warming or shifts in precipitation patterns, or both, have been detected worldwide. The future social impacts of climate change will be uneven across the world.[156] All regions are at risk of experiencing negative impacts,[157] with low-latitude, less developed areas facing the greatest risk.[158] Global warming has likely already increased global economic inequality, and is projected to do so in the future.[159] Regional impacts of climate change are now observable on all continents and across ocean regions.[160] The Arctic, Africa, small islands and Asian megadeltas are regions that are likely to be especially affected by future climate change.[161] Many risks increase with higher magnitudes of global warming.[162] Food and water Crop production will probably be negatively affected in low latitude countries, while effects at northern latitudes may be positive or negative.[163] Global warming of around 4 °C relative to late 20th century levels could pose a large risk to global and regional food security.[164] The impact of climate change on crop productivity for the four major crops was negative for wheat and maize, and neutral for soy and rice, in the years 1960–2013.[165] Climate variability and change is projected to severely compromise agricultural production, including access to food, across Africa.[166] By 2050, between 350 million and 600 million people are projected to experience increased water stress due to climate change in Africa.[166] Water availability will also become more limited in regions dependent on glacier water, regions with reductions in rainfall and small islands.[166] Health and security Aerial view over southern Bangladesh after the passage of cyclone Cyclone Sidr. A combination of sea level rise and increased rainfall from cyclones makes countries more vulnerable to floods, impacting people's livelihoods and health.[167] Generally impacts on public health will be more negative than positive.[168] Impacts include the direct effects of extreme weather, leading to injury and loss of life;[169] and indirect effects, such as undernutrition brought on by crop failures.[170] There has been a shift from cold- to heat-related mortality in some regions as a result of warming.[160] Temperature rise has been connected to increased numbers of suicides.[171] Climate change has been linked to an increase in violent conflict by amplifying poverty and economic shocks, which are well-documented drivers of these conflicts.[172] Links have been made between a wide range of violent behaviour including fist fights, violent crimes, civil unrest, or wars.[173] Livelihoods, industry and infrastructure In small islands and mega deltas, inundation as a result of sea level rise is expected to threaten vital infrastructure and human settlements.[174] This could lead to issues of homelessness in countries with low-lying areas such as Bangladesh, as well as statelessness for populations in island nations, such as the Maldives and Tuvalu.[175] Climate change can be an important driver of migration, both within and between countries.[176][177] Africa is one of the most vulnerable continents to climate variability and change because of multiple existing stresses and low adaptive capacity.[166] Existing stresses include poverty, political conflicts, and ecosystem degradation. Regions may even become uninhabitable, with humidity and temperature reaching levels too high for humans to survive.[178] Responses Mitigation of and adaptation to climate change are two complementary responses to global warming. Successful adaptation is easier in the case of substantial emission reduction. Many of the countries that contributed least to global greenhouse gas emissions are most vulnerable to climate change, which raises questions about justice and fairness with regard to mitigation and adaptation.[179] Mitigation Main article: Climate change mitigation Refer to caption and image description The graph on the right shows three pathways to meet the UNFCCC's 2 °C target, labelled global technology, decentralized solutions, and consumption change. Each pathway shows how various measures (e.g., improved energy efficiency, increased use of renewable energy) could contribute to emissions reductions. Image credit: PBL Netherlands Environmental Assessment Agency.[180] Annual greenhouse gas emissions attributed to different sectors as of the year 2010. Emissions are given as a percentage share of total emissions, measured in carbon dioxide-equivalents, using global warming potentials from the IPCC fifth Assessment Report. Mitigation of climate change is the reduction of greenhouse gas emissions, or the enhancement of the capacity of carbon sinks to absorb greenhouse gases from the atmosphere.[181] There is a large potential for future reductions in emissions by a combination of activities, including energy conservation and increased energy efficiency; the use of low-carbon energy technologies, such as renewable energy, nuclear energy, and carbon capture and storage; decarbonizing buildings and transport; and enhancing carbon sinks through, for example, reforestation and preventing deforestation.[182][183] A 2015 report by Citibank concluded that transitioning to a low carbon economy would yield positive return on investments.[184] Global carbon dioxide emissions by country in 2015 Drivers of greenhouse gas emissions Over the last three decades of the twentieth century, gross domestic product per capita and population growth were the main drivers of increases in greenhouse gas emissions.[185] CO2 emissions are continuing to rise due to the burning of fossil fuels and land-use change.[186] Emissions can be attributed to different regions. Attribution of emissions due to land-use change are subject to considerable uncertainty.[187] Emissions scenarios, estimates of changes in future emission levels of greenhouse gases, have been projected that depend upon uncertain economic, sociological, technological, and natural developments.[188] In some scenarios emissions continue to rise over the century, while others have reduced emissions.[189] Fossil fuel reserves are abundant, and will not limit carbon emissions in the 21st century.[190] Emission scenarios, combined with modelling of the carbon cycle, have been used to produce estimates of how atmospheric concentrations of greenhouse gases might change in the future.[191] Depending both on the Shared Socioeconomic Pathway (SSP) the world takes and the mitigation scenario, model suggest that by the year 2100, the atmospheric concentration of CO2 could range between 380 and 1400 ppm.[192] Reducing greenhouse gases Near- and long-term trends in the global energy system are inconsistent with limiting global warming at below 1.5 or 2 °C, relative to pre-industrial levels.[193] Current pledges made as part of the Paris Agreement would lead to about 3.0 °C of warming at the end of the 21st century, relative to pre-industrial levels.[194] In limiting warming at below 2 °C, more stringent emission reductions in the near-term would allow for less rapid reductions after 2030,[195] and be cheaper overall.[196] Many integrated models are unable to meet the 2 °C target if pessimistic assumptions are made about the availability of mitigation technologies.[197] Co-benefits of climate change mitigation may help society and individuals more quickly. For example, cycling reduces greenhouse gas emissions[198] while reducing the effects of a sedentary lifestyle at the same time.[199] The development and scaling-up of clean technology, such as cement that produces less CO2.[200] is critical to achieve sufficient emission reductions for the Paris agreement goals.[201] It has been suggested that the most effective and comprehensive policy to reduce carbon emissions is a carbon tax[202] or the closely related emissions trading.[203] There are diverse opinions on how people could mitigate their carbon footprint. One suggestion is that the best approach is having fewer children, and to a lesser extent living car-free, forgoing air travel, and adopting a plant-based diet.[204] Some disagree with encouraging people to stop having children, saying that children embody a profound hope for the future, and that more emphasis should be placed on overconsumption, lifestyle choices of the world's wealthy, fossil fuel companies and government inaction.[205] Still others, such as Mayer Hillman, contend that both individual action and political action by national governments will not be enough, and only a global transition to zero GHG emissions throughout the entire economy and a reduction in human population growth will be sufficient to mitigate global warming.[206] Adaptation Main article: Climate change adaptation Climate change adaptation is the process of adjusting to actual or expected climate and its effects.[207] Humans can strive to moderate or avoid harm due to climate change and exploit opportunities.[207] Examples of adaptation are improved coastline protection, better disaster management and the development of crops that are more resistant.[208] The adaptation may be planned, either in reaction to or anticipation of global warming, or spontaneous, i.e., without government intervention.[209] The public section, private sector and communities are all gaining experience with adaptation and adaptation is becoming embedded within certain planning processes.[210] While some adaptation responses call for trade-offs, others bring synergies and co-benefits.[210] Environmental organizations and public figures have emphasized changes in the climate and the risks they entail, while promoting adaptation to changes in infrastructural needs and emissions reductions.[211] Adaptation is especially important in developing countries since those countries are predicted to bear the brunt of the effects of global warming.[212] That is, the capacity and potential for humans to adapt, called adaptive capacity, is unevenly distributed across different regions and populations, and developing countries generally have less capacity to adapt.[213] In June 2019, U.N. special rapporteur Philip Alston warned of a 'climate apartheid' situation developing, where global warming could push more than 120 million more people into poverty by 2030 and will have the most severe impact in poor countries, regions, and the places poor people live and work.[214] Climate engineering Main article: Climate engineering Climate engineering (sometimes called geoengineering or climate intervention) is the deliberate modification of the climate. It has been investigated as a possible response to global warming, e.g. by NASA[215] and the Royal Society.[216] Techniques under research fall generally into the categories solar radiation management and carbon dioxide removal, although various other schemes have been suggested. A study from 2014 investigated the most common climate engineering methods and concluded they are either ineffective or have potentially severe side effects and cannot be stopped without causing rapid climate change.[217] Society and culture Political response Main article: Politics of global warming refer to caption Article 2 of the UN Framework Convention refers explicitly to stabilization of greenhouse gas concentrations.[218] To stabilize the atmospheric concentration of CO 2, emissions worldwide would need to be dramatically reduced from their present level.[219] As of 2019 all countries in the world are parties to the United Nations Framework Convention on Climate Change (UNFCCC), but 12 countries have not ratified it,[220] which means they are not legally bound by the agreement.[221] The ultimate objective of the Convention is to prevent dangerous human interference to the climate system.[222] As stated in the Convention, this requires that greenhouse gas concentrations are stabilized in the atmosphere at a level where ecosystems can adapt naturally to climate change, food production is not threatened, and economic development can be sustained.[223] The Framework Convention was agreed on in 1992, but global emissions have risen since then.[224] Its yearly conferences are the stage of global negotiations.[225] During these negotiations, the G77 (a lobbying group in the United Nations representing developing countries)[226] pushed for a mandate requiring developed countries to [take] the lead in reducing their emissions.[227] This was justified on the basis that the developed countries' emissions had contributed most to the accumulation of greenhouse gases in the atmosphere, per-capita emissions (i.e., emissions per head of population) were still relatively low in developing countries, and the emissions of developing countries would grow to meet their development needs.[228] This mandate was sustained in the 2005 Kyoto Protocol to the Framework Convention.[229] In ratifying the Kyoto Protocol, most developed countries accepted legally binding commitments to limit their emissions. These first-round commitments expired in 2012.[230] United States President George W. Bush rejected the treaty on the basis that it exempts 80% of the world, including major population centres such as China and India, from compliance, and would cause serious harm to the US economy.[231] In 2009 several UNFCCC Parties produced the Copenhagen Accord,[232] which has been widely portrayed as disappointing because of its low goals, leading poor nations to reject it.[233] Parties associated with the Accord aim to limit the future increase in global mean temperature to below 2 °C.[234] In 2015 all UN countries negotiated the Paris Agreement, which aims to keep climate change well below 2 °C. The agreement replaced the Kyoto protocol. Unlike Kyoto, no binding emission targets are set in the Paris agreement. Instead, the procedure of regularly setting ever more ambitious goals and reevaluating these goals every five years has been made binding.[235] The Paris agreement reiterated that developing countries must be financially supported.[235] Scientific discussion Main article: Scientific consensus on climate change In the scientific literature, there is an overwhelming consensus that global surface temperatures have increased in recent decades and that the trend is caused mainly by human-induced emissions of greenhouse gases.[236] No scientific body of national or international standing disagrees with this view.[237] Scientific discussion takes place in journal articles that are peer-reviewed, which scientists subject to assessment every couple of years in the Intergovernmental Panel on Climate Change reports.[238] The scientific consensus as of 2013 stated in the IPCC Fifth Assessment Report is that it is extremely likely that human influence has been the dominant cause of the observed warming since the mid-20th century.[239] National science academies have called on world leaders for policies to cut global emissions.[240] In November 2017, a second warning to humanity signed by 15,364 scientists from 184 countries stated that the current trajectory of potentially catastrophic climate change due to rising greenhouse gases from burning fossil fuels, deforestation, and agricultural production – particularly from farming ruminants for meat consumption is especially troubling.[241] In 2018 the IPCC published a Special Report on Global Warming of 1.5 °C which warned that, if the current rate of greenhouse gas emissions is not mitigated, global warming is likely to reach 1.5 °C (2.7 °F) between 2030 and 2052 risking major crises. The report said that preventing such crises will require a swift transformation of the global economy that has no documented historic precedent.[242] Fossil fuel companies See also: Fossil fuels lobby In the 20th century and early 2000s some companies, such as ExxonMobil, challenged IPCC climate change scenarios, funded scientists who disagreed with the scientific consensus, and provided their own projections of the economic cost of stricter controls.[243] In general, since the 2010s, global oil companies do not dispute that climate change exists and is caused by the burning of fossil fuels.[244] As of 2019, however, some are lobbying against a carbon tax and plan to increase production of oil and gas[245] but others are in favour of a carbon tax in exchange for immunity from lawsuits which seek climate change compensation.[246] Public opinion and disputes Further information: Climate change denial, Media coverage of climate change, and Public opinion on climate change Global warming was the cover story in this 2007 issue of Ms. magazine The global warming problem came to international public attention in the late 1980s.[247] Significant regional differences exists in how concerned people are about climate change and how much they understand the issue.[22] In 2010, just a little over half the US population viewed it as a serious concern for either themselves or their families, while people in Latin America and developed Asia saw themselves most at risk at 73% and 74%.[248] Similarly, in 2015 a median of 54% of respondents consider it a very serious problem, Americans and Chinese (whose economies are responsible for the greatest annual CO2 emissions) were among the least concerned.[22] Worldwide in 2011, people were more likely to attribute global warming to human activities than to natural causes, except in the US where nearly half of the population attributed global warming to natural causes.[249] Public reactions to global warming and concern about its effects have been increasing, with many perceiving it as the worst global threat.[250] From about 1990 onward, American conservative think tanks had begun challenging the legitimacy of global warming as a social problem. They challenged the scientific evidence, argued that global warming would have benefits, and asserted that proposed solutions would do more harm than good.[251] Organizations such as the libertarian Competitive Enterprise Institute, conservative commentators have challenged IPCC climate change scenarios, funded scientists who disagree with the scientific consensus, and provided their own projections of the economic cost of stricter controls.[252] Global warming has been the subject of controversy, substantially more pronounced in the popular media than in the scientific literature,[253] with disputes regarding the nature, causes, and consequences of global warming. The disputed issues include the causes of increased global average air temperature, especially since the mid-20th century, whether this warming trend is unprecedented or within normal climatic variations, whether humankind has contributed significantly to it, and whether the increase is completely or partially an artifact of poor measurements. Additional disputes concern estimates of climate sensitivity, predictions of additional warming, what the consequences of global warming will be, and what to do about it.[254] Due to confusing media coverage in the early 1990s, issues such as ozone depletion and climate change were often mixed up, affecting public understanding of these issues.[255] Although there are a few areas of linkage, the relationship between the two is weak.[256] However, chemicals causing ozone depletion are also powerful greenhouse gases, and as such the Montreal protocol against their emissions may have done more than any other measure to mitigate climate change.[257] The climate movement In a response to perceived inaction on climate change, a climate movement is protesting in various ways, such as fossil fuel divestment,[258] worldwide demonstrations[259] and the school strike for climate.[260] Climate change is increasingly a theme in art, literature and film.[citation needed] Mass civil disobedience actions by Extinction Rebellion and Ende Gelände have ended in police intervention large-scale arrests.[261][262][263] History of the Science Scientific American description of 1856 Eunice Newton Foote's experiments which found that carbonic acid (CO2) causes warming. The history of climate change science began in the early 19th century when ice ages and other natural changes in paleoclimate were first suspected and the natural greenhouse effect first identified.[264] In the late 19th century, scientists first argued that human emissions of greenhouse gases could change the climate. In the 1960s, the warming effect of carbon dioxide gas became increasingly convincing.[265] By the 1990s, as a result of improving fidelity of computer models and observational work confirming the Milankovitch theory of the ice ages, a consensus position formed: greenhouse gases were deeply involved in most climate changes, and human-caused emissions were bringing discernible global warming. Since then, scientific research on climate change has expanded.[266] The Intergovernmental Panel on Climate Change, set up in the 1990s to provide formal advice the world's governments, spurred unprecedented levels of exchange between different scientific disciplines.[267] The greenhouse effect was proposed by Joseph Fourier in 1824, discovered in 1856 by Eunice Newton Foote,[268] expanded upon by John Tyndall,[269] investigated quantitatively by Svante Arrhenius in 1896,[264] and the hypothesis was reported in the popular press as early as 1912.[270] The scientific description of global warming was further developed in the 1930s through the 1960s by Guy Stewart Callendar.[271] Terminology Research in the 1950s suggested increasing temperatures, and a 1952 newspaper reported climate change. This phrase next appeared in a November 1957 report in The Hammond Times which described Roger Revelle's research into the effects of increasing human-caused CO 2 emissions on the greenhouse effect a large scale global warming, with radical climate changes may result. A 1971 MIT report, referred to the human impact as inadvertent climate modification, identifying many possible causes.[272] Both the terms global warming and climate change were used only occasionally until 1975, when Wallace Smith Broecker published a scientific paper on the topic, Climatic Change: Are We on the Brink of a Pronounced Global Warming? The phrase began to come into common use, and in 1976 Mikhail Budyko's statement that a global warming up has started was widely reported.[265] An influential 1979 National Academy of Sciences study headed by Jule Charney followed Broecker in using global warming to refer to rising surface temperatures, while describing the wider effects of increased CO 2 as climate change.[273] There were increasing heatwaves and drought problems in the summer of 1988, and when NASA climate scientist James Hansen gave testimony in the U.S. Senate, it sparked worldwide interest.[266] He said global warming has reached a level such that we can ascribe with a high degree of confidence a cause and effect relationship between the greenhouse effect and the observed warming.[274] Public attention increased over the summer, and global warming became the dominant popular term, commonly used both by the press and in public discourse.[273] In the 2000s, the term climate change increased in popularity.[275] People who regard climate change as catastrophic, irreversible or rapid might label climate change as a climate crisis or a climate emergency.[276] Some major newspapers, such as The Guardian, have taken up the use of this terminology, as well as the term global heating, in order to emphasize its seriousness and urgency.[277] Since 2016, some city councils have issued climate emergency declarations.[278][279] In 2019, the British Parliament became the first national government in the world to officially declare a climate emergency.[280]")

#creates the cloud
wave_mask = np.array(Image.open( "cloud5.jpg"))
wordcloud = WordCloud(width=600, height=600, margin=0, mask=wave_mask).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

init_notebook_mode(connected=True)
iplot(plotly_wordcloud(text))


# In[ ]:




