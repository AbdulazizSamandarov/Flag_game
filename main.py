import random
from tkinter import *

names_and_flags = [
    {
        "name": "algeria",
        "flag": "images/algeria.png"
    },
    {
        "name": "andorra",
        "flag": "images/andorra.png"
    },
    {
        "name": "albania",
        "flag": "images/albania.png"
    },
    {
        "name": "afganistan",
        "flag": "images/afganistan.png"
    },
    {
        "name": "angola",
        "flag": "images/angola.png"
    },
    {
        "name": "antarctica",
        "flag": "images/antarctica.png"
    },
    {
        "name": "antigua_and_barbuda",
        "flag": "images/antigua_and_barbuda.png"
    },
    {
        "name": "argentina",
        "flag": "images/argentina.png"
    },
    {
        "name": "armenia",
        "flag": "images/armenia.png"
    },
    {
        "name": "artsakh",
        "flag": "images/artsakh.png"
    },
    {
        "name": "australia",
        "flag": "images/australia.png"
    },
    {
        "name": "austria",
        "flag": "images/austria.png"
    },
    {
        "name": "azerbaijan",
        "flag": "images/azerbaijan.png"
    },
    {
        "name": "bahamas",
        "flag": "images/bahamas.png"
    },
    {
        "name": "bahrain",
        "flag": "images/bahrain.png"
    },
    {
        "name": "bangladesh",
        "flag": "images/bangladesh.png"
    },
    {
        "name": "barbados",
        "flag": "images/barbados.png"
    },
    {
        "name": "belarus",
        "flag": "images/belarus.png"
    },
    {
        "name": "belgium",
        "flag": "images/belgium.png"
    },
    {
        "name": "belize",
        "flag": "images/belize.png"
    },
    {
        "name": "benin",
        "flag": "images/benin.png"
    },
    {
        "name": "bhutan",
        "flag": "images/bhutan.png"
    },
    {
        "name": "bolivia",
        "flag": "images/bolivia.png"
    },
    {
        "name": "bosnia",
        "flag": "images/bosnia.png"
    },
    {
        "name": "botswana",
        "flag": "images/botswana.png"
    },
    {
        "name": "brazil",
        "flag": "images/brazil.png"
    },
    {
        "name": "brunei",
        "flag": "images/brunei.png"
    },
    {
        "name": "bulgaria",
        "flag": "images/bulgaria.png"
    },
    {
        "name": "burkina",
        "flag": "images/burkina.png"
    },
    {
        "name": "burundi",
        "flag": "images/burundi.png"
    },
    {
        "name": "cambodia",
        "flag": "images/cambodia.png"
    },
    {
        "name": "cameroon",
        "flag": "images/cameroon.png"
    },
    {
        "name": "canada",
        "flag": "images/canada.png"
    },
    {
        "name": "cape_verde",
        "flag": "images/cape_verde.png"
    },
    {
        "name": "central_african_republic",
        "flag": "images/central_african_republic.png"
    },
    {
        "name": "chad",
        "flag": "images/chad.png"
    },
    {
        "name": "chile",
        "flag": "images/chile.png"
    },
    {
        "name": "colombia",
        "flag": "images/colombia.png"
    },
    {
        "name": "comoros",
        "flag": "images/comoros.png"
    },
    {
        "name": "cook_islands",
        "flag": "images/cook_islands.png"
    },
    {
        "name": "costa_rica",
        "flag": "images/costa_rica.png"
    },
    {
        "name": "croatia",
        "flag": "images/croatia.png"
    },
    {
        "name": "cuba",
        "flag": "images/cuba.png"
    },
    {
        "name": "cyprus",
        "flag": "images/cyprus.png"
    },
    {
        "name": "czech",
        "flag": "images/czech.png"
    },
    {
        "name": "denmark",
        "flag": "images/denmark.png"
    },
    {
        "name": "djibouti",
        "flag": "images/djibouti.png"
    },
    {
        "name": "dominica",
        "flag": "images/dominica.png"
    },
    {
        "name": "dominican_republic",
        "flag": "images/dominican_republic.png"
    },
    {
        "name": "east_timor",
        "flag": "images/east_timor.png"
    },
    {
        "name": "ecuador",
        "flag": "images/ecuador.png"
    },
    {
        "name": "egypt",
        "flag": "images/egypt.png"
    },
    {
        "name": "el_salvador",
        "flag": "images/el_salvador.png"
    },
    {
        "name": "england",
        "flag": "images/england.png"
    },
    {
        "name": "equatorial_guinea",
        "flag": "images/equatorial_guinea.png"
    },
    {
        "name": "eritrea",
        "flag": "images/eritrea.png"
    },
    {
        "name": "estonia",
        "flag": "images/estonia.png"
    },
    {
        "name": "eswatini",
        "flag": "images/eswatini.png"
    },
    {
        "name": "ethiopia",
        "flag": "images/ethiopia.png"
    },
    {
        "name": "federated_states_of_micronesia",
        "flag": "images/federated_states_of_micronesia.png"
    },
    {
        "name": "fiji",
        "flag": "images/fiji.png"
    },
    {
        "name": "finland",
        "flag": "images/finland.png"
    },
    {
        "name": "france",
        "flag": "images/france.png"
    },
    {
        "name": "gabon",
        "flag": "images/gabon.png"
    },
    {
        "name": "gambia",
        "flag": "images/gambia.png"
    },
    {
        "name": "georgia",
        "flag": "images/georgia.png"
    },
    {
        "name": "germany",
        "flag": "images/germany.png"
    },
    {
        "name": "ghana",
        "flag": "images/ghana.png"
    },
    {
        "name": "greece",
        "flag": "images/greece.png"
    },
    {
        "name": "grenada",
        "flag": "images/grenada.png"
    },
    {
        "name": "guatemala",
        "flag": "images/guatemala.png"
    },
    {
        "name": "guinea",
        "flag": "images/guinea.png"
    },
    {
        "name": "guinea_bissau",
        "flag": "images/guinea_bissau.png"
    },
    {
        "name": "guyana",
        "flag": "images/guyana.png"
    },
    {
        "name": "haiti",
        "flag": "images/haiti.png"
    },
    {
        "name": "honduras",
        "flag": "images/honduras.png"
    },
    {
        "name": "hong_kong",
        "flag": "images/hong_kong.png"
    },
    {
        "name": "hungary",
        "flag": "images/hungary.png"
    },
    {
        "name": "iceland",
        "flag": "images/iceland.png"
    },
    {
        "name": "india",
        "flag": "images/india.png"
    },
    {
        "name": "indonesia",
        "flag": "images/indonesia.png"
    },
    {
        "name": "iran",
        "flag": "images/iran.png"
    },
    {
        "name": "iraq",
        "flag": "images/iraq.png"
    },
    {
        "name": "ireland",
        "flag": "images/ireland.png"
    },
    {
        "name": "israel",
        "flag": "images/israel.png"
    },
    {
        "name": "italy",
        "flag": "images/italy.png"
    },
    {
        "name": "jamaica",
        "flag": "images/jamaica.png"
    },
    {
        "name": "japan",
        "flag": "images/japan.png"
    },
    {
        "name": "jordan",
        "flag": "images/jordan.png"
    },
    {
        "name": "kazakhstan",
        "flag": "images/kazakhstan.png"
    },
    {
        "name": "kenya",
        "flag": "images/kenya.png"
    },
    {
        "name": "kiribati",
        "flag": "images/kiribati.png"
    },
    {
        "name": "kosova",
        "flag": "images/kosova.png"
    },
    {
        "name": "kuwait",
        "flag": "images/kuwait.png"
    },
    {
        "name": "kyrgyzstan",
        "flag": "images/kyrgyzstan.png"
    },
    {
        "name": "laos",
        "flag": "images/laos.png"
    },
    {
        "name": "latvia",
        "flag": "images/latvia.png"
    },
    {
        "name": "lebanon",
        "flag": "images/lebanon.png"
    },
    {
        "name": "lesotho",
        "flag": "images/lesotho.png"
    },
    {
        "name": "liberia",
        "flag": "images/liberia.png"
    },
    {
        "name": "libya",
        "flag": "images/libya.png"
    },
    {
        "name": "libya",
        "flag": "images/libya.png"
    },
    {
        "name": "liechtenstein",
        "flag": "images/liechtenstein.png"
    },
    {
        "name": "lithuania",
        "flag": "images/lithuania.png"
    },
    {
        "name": "luxembourg",
        "flag": "images/luxembourg.png"
    },
    {
        "name": "madagascar",
        "flag": "images/madagascar.png"
    },
    {
        "name": "malawi",
        "flag": "images/malawi.png"
    },
    {
        "name": "malaysia",
        "flag": "images/malaysia.png"
    },
    {
        "name": "mali",
        "flag": "images/mali.png"
    },
    {
        "name": "malta",
        "flag": "images/malta.png"
    },
    {
        "name": "marshall_islands",
        "flag": "images/marshall_islands.png"
    },
    {
        "name": "mauritania",
        "flag": "images/mauritania.png"
    },
    {
        "name": "mauritius",
        "flag": "images/mauritius.png"
    },
    {
        "name": "mexico",
        "flag": "images/mexico.png"
    },
    {
        "name": "moldova",
        "flag": "images/moldova.png"
    },
    {
        "name": "monaco",
        "flag": "images/monaco.png"
    },
    {
        "name": "mongolia",
        "flag": "images/mongolia.png"
    },
    {
        "name": "montenegro",
        "flag": "images/montenegro.png"
    },
    {
        "name": "morocco",
        "flag": "images/morocco.png"
    },
    {
        "name": "mozambique",
        "flag": "images/mozambique.png"
    },
    {
        "name": "myanmar",
        "flag": "images/myanmar.png"
    },
    {
        "name": "namibia",
        "flag": "images/namibia.png"
    },
    {
        "name": "nauru",
        "flag": "images/nauru.png"
    },
    {
        "name": "nepal",
        "flag": "images/nepal.png"
    },
    {
        "name": "netherlands",
        "flag": "images/netherlands.png"
    },
    {
        "name": "new_zealand",
        "flag": "images/new_zealand.png"
    },
    {
        "name": "nicaragua",
        "flag": "images/nicaragua.png"
    },
    {
        "name": "niger",
        "flag": "images/niger.png"
    },
    {
        "name": "nigeria",
        "flag": "images/nigeria.png"
    },
    {
        "name": "niue",
        "flag": "images/niue.png"
    },
    {
        "name": "north_korea",
        "flag": "images/north_korea.png"
    },
    {
        "name": "north_macedonia",
        "flag": "images/north_macedonia.png"
    },
    {
        "name": "norway",
        "flag": "images/norway.png"
    },
    {
        "name": "oman",
        "flag": "images/oman.png"
    },
    {
        "name": "pakistan",
        "flag": "images/pakistan.png"
    },
    {
        "name": "palau",
        "flag": "images/palau.png"
    },
    {
        "name": "palestine",
        "flag": "images/palestine.png"
    },
    {
        "name": "panama",
        "flag": "images/panama.png"
    },
    {
        "name": "papua_new_guinea",
        "flag": "images/papua_new_guinea.png"
    },
    {
        "name": "paraguay",
        "flag": "images/paraguay.png"
    },
    {
        "name": "peru",
        "flag": "images/peru.png"
    },
    {
        "name": "philippines",
        "flag": "images/philippines.png"
    },
    {
        "name": "poland",
        "flag": "images/poland.png"
    },
    {
        "name": "portugal",
        "flag": "images/portugal.png"
    },
    {
        "name": "qatar",
        "flag": "images/qatar.png"
    },
    {
        "name": "republic_of_abkhazia",
        "flag": "images/republic_of_abkhazia.png"
    },
    {
        "name": "republic_of_congo",
        "flag": "images/republic_of_congo.png"
    },
    {
        "name": "romania",
        "flag": "images/romania.png"
    },
    {
        "name": "russia",
        "flag": "images/russia.png"
    },
    {
        "name": "rwanda",
        "flag": "images/rwanda.png"
    },
    {
        "name": "sahrawi_arab_democratic_republic",
        "flag": "images/sahrawi_arab_democratic_republic.png"
    },
    {
        "name": "saint_kitts_and_nevis",
        "flag": "images/saint_kitts_and_nevis.png"
    },
    {
        "name": "saint_lucia",
        "flag": "images/saint_lucia.png"
    },
    {
        "name": "saint_vincent_and_the_grenadines",
        "flag": "images/saint_vincent_and_the_grenadines.png"
    },
    {
        "name": "samoa",
        "flag": "images/samoa.png"
    },
    {
        "name": "san_marino",
        "flag": "images/san_marino.png"
    },
    {
        "name": "sao_tome",
        "flag": "images/sao_tome.png"
    },
    {
        "name": "saudi_arabia",
        "flag": "images/saudi_arabia.png"
    },
    {
        "name": "scotland",
        "flag": "images/scotland.png"
    },
    {
        "name": "senegal",
        "flag": "images/senegal.png"
    },
    {
        "name": "serbia",
        "flag": "images/serbia.png"
    },
    {
        "name": "seychelles",
        "flag": "images/seychelles.png"
    },
    {
        "name": "sierra_leone",
        "flag": "images/sierra_leone.png"
    },
    {
        "name": "singapore",
        "flag": "images/singapore.png"
    },
    {
        "name": "slovakia",
        "flag": "images/slovakia.png"
    },
    {
        "name": "slovenia",
        "flag": "images/slovenia.png"
    },
    {
        "name": "solomon",
        "flag": "images/solomon.png"
    },
    {
        "name": "somalia",
        "flag": "images/somalia.png"
    },
    {
        "name": "somaliland",
        "flag": "images/somaliland.png"
    },
    {
        "name": "south_africa",
        "flag": "images/south_africa.png"
    },
    {
        "name": "south_korea",
        "flag": "images/south_korea.png"
    },
    {
        "name": "south_ossetia",
        "flag": "images/south_ossetia.png"
    },
    {
        "name": "south_sudan",
        "flag": "images/south_sudan.png"
    },
    {
        "name": "spain",
        "flag": "images/spain.png"
    },
    {
        "name": "srilanka",
        "flag": "images/srilanka.png"
    },
    {
        "name": "sudan",
        "flag": "images/sudan.png"
    },
    {
        "name": "suriname",
        "flag": "images/suriname.png"
    },
    {
        "name": "sweden",
        "flag": "images/sweden.png"
    },
    {
        "name": "switzerland",
        "flag": "images/switzerland.png"
    },
    {
        "name": "syria",
        "flag": "images/syria.png"
    },
    {
        "name": "taiwan",
        "flag": "images/taiwan.png"
    },
    {
        "name": "tajikistan",
        "flag": "images/tajikistan.png"
    },
    {
        "name": "tanzania",
        "flag": "images/tanzania.png"
    },
    {
        "name": "thailand",
        "flag": "images/thailand.png"
    },
    {
        "name": "togo",
        "flag": "images/togo.png"
    },
    {
        "name": "transnistria",
        "flag": "images/transnistria.png"
    },
    {
        "name": "trinidad",
        "flag": "images/trinidad.png"
    },
    {
        "name": "tunisia",
        "flag": "images/tunisia.png"
    },
    {
        "name": "turkey",
        "flag": "images/turkey.png"
    },
    {
        "name": "turkish_republic_of_northern_cyprus",
        "flag": "images/turkish_republic_of_northern_cyprus.png"
    },
    {
        "name": "turkmenistan",
        "flag": "images/turkmenistan.png"
    },
    {
        "name": "tuvalu",
        "flag": "images/tuvalu.png"
    },
    {
        "name": "uganda",
        "flag": "images/uganda.png"
    },
    {
        "name": "ukraine",
        "flag": "images/ukraine.png"
    },
    {
        "name": "united_arab_emirates",
        "flag": "images/united_arab_emirates.png"
    },
    {
        "name": "united_kingdom",
        "flag": "images/united_kingdom.png"
    },
    {
        "name": "united_states_of_america",
        "flag": "images/united_states_of_america.png"
    },
    {
        "name": "uruguay",
        "flag": "images/uruguay.png"
    },
    {
        "name": "uzbekistan",
        "flag": "images/uzbekistan.png"
    },
    {
        "name": "vanuatu",
        "flag": "images/vanuatu.png"
    },
    {
        "name": "vatican",
        "flag": "images/vatican.png"
    },
    {
        "name": "venezuela",
        "flag": "images/venezuela.png"
    },
    {
        "name": "vietnam",
        "flag": "images/vietnam.png"
    },
    {
        "name": "wales",
        "flag": "images/wales.png"
    },
    {
        "name": "yemen",
        "flag": "images/yemen.png"
    },
    {
        "name": "zambia",
        "flag": "images/zambia.png"
    },
    {
        "name": "zimbabwe",
        "flag": "images/zimbabwe.png"
    }
]
data = random.choice(names_and_flags)
print(data['name'])
print(data['flag'])

BACKGROUND_COLOR = "#37306B"
window = Tk()
window.title('Flag game')
window.config(padx=150, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=256, height=256, highlightthickness=0, bg=BACKGROUND_COLOR)
photo = PhotoImage(file=data['flag'])
canvas.create_image(128, 128, image=photo)
canvas.grid(row=0, column=1, pady=20, padx=20)

guess = Entry(width=42)
guess.grid(row=1, column=1)

result = Label(text="", bg=BACKGROUND_COLOR, fg="White", font=("Arier", 20, 'bold'))
result.grid(row=2, column=1)


def increase():
    global high_score
    high_score += 1

def increase_overall():
    global overall
    overall +=1

overall = 0
high_score = 0
score = Label(text=f"{overall}/{high_score}", bg=BACKGROUND_COLOR, fg="White", font=("Arier", 40, 'bold'))
score.grid(row=0, column=3)

answer = Label(text="", bg=BACKGROUND_COLOR, fg="White", font=("Arier", 20, 'bold'))
answer.grid(row=3, column=1)


def skipping():
    skip.config(text="   Skip  ")
    answer.config(text="")
    result.config(text="", fg="white")
    info = random.choice(names_and_flags)
    photo.config(file=info['flag'])
    data['name'] = info['name']
    guess.delete(first=0, last=220)


def search_it():

    try:
        my_search = f"images/{search.get()}.png"
        photo.config(file=my_search)
        data['name'] = search.get()
        answer.config(text="")
        result.config(text="", fg="white")
    except:
        TclError

    guess.delete(first=0, last=220)
    search.delete(first=0, last=220)


def check():
    increase_overall()
    score.config(text=f"{overall}/{high_score}")
    if guess.get().lower() == data['name']:
        result.config(text="True", fg="green")
        answer.config(text=f"it was {data['name']}")
        increase()
        score.config(text=f"{overall}/{high_score}")
        skip.config(text="   Next   ")
    else:
        result.config(text="Wrong", fg="red")
        answer.config(text=f"it was {data['name']}")

    skip.config(text="   Next   ")
    info = random.choice(names_and_flags)
    photo.config(file=info['flag'])
    data['name'] = info['name']
    guess.delete(first=0, last=220)


submit = Button(text="Submit", bg=BACKGROUND_COLOR, fg="White", command=check)
submit.grid(row=1, column=2)

skip = Button(text="   Skip  ", bg=BACKGROUND_COLOR, fg="White", command=skipping)
skip.grid(row=2, column=2, pady=10)

search = Entry(width=42)
search.grid(row=4, column=1, pady=10)

search_button = Button(text="Search", bg=BACKGROUND_COLOR, fg="White", command=search_it)
search_button.grid(row=4, column=2, pady=10)

window.mainloop()
