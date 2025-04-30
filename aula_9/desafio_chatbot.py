import streamlit as st
import requests

# Exemplo de dicionário de mapeamento com todos os países do mundo em português para inglês.
mapa_paises = {
    "afeganistão": "afghanistan",
    "áfrica do sul": "south africa",
    "albania": "albania",
    "alemanha": "germany",
    "andorra": "andorra",
    "angola": "angola",
    "antígua e barbuda": "antigua and barbuda",
    "argélia": "algeria",
    "argentina": "argentina",
    "armênia": "armenia",
    "austrália": "australia",
    "áustria": "austria",
    "azerbaijão": "azerbaijan",
    "bahamas": "bahamas",
    "bahrein": "bahrain",
    "bangladesh": "bangladesh",
    "barbados": "barbados",
    "bélgica": "belgium",
    "benin": "benin",
    "butão": "bhutan",
    "bielorrússia": "belarus",
    "birmania": "myanmar",
    "bolívia": "bolivia",
    "bósnia e herzegovina": "bosnia and herzegovina",
    "botswana": "botswana",
    "brasil": "brazil",
    "brunei": "brunei",
    "bulgária": "bulgaria",
    "burkina faso": "burkina faso",
    "burundi": "burundi",
    "cabo verde": "cape verde",
    "cambodja": "cambodia",
    "camarões": "cameroon",
    "canadá": "canada",
    "catar": "qatar",
    "chile": "chile",
    "china": "china",
    "chipre": "cyprus",
    "colômbia": "colombia",
    "comores": "comoros",
    "congo": "congo",
    "coreia do norte": "north korea",
    "coreia do sul": "south korea",
    "cosovo": "kosovo",
    "costa do marfim": "ivory coast",
    "croácia": "croatia",
    "cuba": "cuba",
    "dinamarca": "denmark",
    "djibuti": "djibouti",
    "dominica": "dominica",
    "egito": "egypt",
    "el salvador": "el salvador",
    "emirados árabes unidos": "united arab emirates",
    "equador": "ecuador",
    "eritrea": "eritrea",
    "espanha": "spain",
    "estados unidos": "united states",
    "estónia": "estonia",
    "eswatini": "eswatini",
    "etiópia": "ethiopia",
    "fiji": "fiji",
    "filipinas": "philippines",
    "finlândia": "finland",
    "frança": "france",
    "gabão": "gabon",
    "gambia": "gambia",
    "gana": "ghana",
    "grécia": "greece",
    "grenada": "grenada",
    "guatemala": "guatemala",
    "guiné": "guinea",
    "guiné-bissau": "guinea-bissau",
    "guiana": "guyana",
    "haiti": "haiti",
    "holanda": "netherlands",
    "hungria": "hungary",
    "índia": "india",
    "indonésia": "indonesia",
    "irã": "iran",
    "iraque": "iraq",
    "irlanda": "ireland",
    "islândia": "iceland",
    "itália": "italy",
    "jamaica": "jamaica",
    "japão": "japan",
    "jordânia": "jordan",
    "kiribati": "kiribati",
    "kuwait": "kuwait",
    "laos": "laos",
    "lesoto": "lesotho",
    "lituânia": "lithuania",
    "líbano": "lebanon",
    "libéria": "liberia",
    "líbia": "libya",
    "liechtenstein": "liechtenstein",
    "luxemburgo": "luxembourg",
    "madagáscar": "madagascar",
    "malawi": "malawi",
    "malásia": "malaysia",
    "maldivas": "maldives",
    "mali": "mali",
    "malta": "malta",
    "marrocos": "morocco",
    "martinica": "martinique",
    "maurício": "mauritius",
    "mauritanía": "mauritania",
    "méxico": "mexico",
    "micronésia": "micronesia",
    "moçambique": "mozambique",
    "moldávia": "moldova",
    "mônaco": "monaco",
    "mongólia": "mongolia",
    "montenegro": "montenegro",
    "namíbia": "namibia",
    "nauru": "nauru",
    "nepal": "nepal",
    "níger": "niger",
    "nicaragua": "nicaragua",
    "nigéria": "nigeria",
    "noruega": "norway",
    "nova zelândia": "new zealand",
    "omã": "oman",
    "paquistão": "pakistan",
    "palau": "palau",
    "panamá": "panama",
    "papua nova guiné": "papua new guinea",
    "paraguai": "paraguay",
    "peru": "peru",
    "polônia": "poland",
    "portugal": "portugal",
    "quênia": "kenya",
    "quiribati": "kiribati",
    "república tcheca": "czech republic",
    "romênia": "romania",
    "ruanda": "rwanda",
    "rússia": "russia",
    "saint kitts e nevis": "saint kitts and nevis",
    "saint lucia": "saint lucia",
    "saint vincent e granadinas": "saint vincent and the grenadines",
    "samoa": "samoa",
    "san marino": "san marino",
    "santa sé": "vatican city",
    "senegal": "senegal",
    "serra leoa": "sierra leone",
    "singapura": "singapore",
    "síria": "syria",
    "somália": "somalia",
    "sri lanka": "sri lanka",
    "suazilândia": "swaziland",
    "sudão": "sudan",
    "suriname": "suriname",
    "suécia": "sweden",
    "suíça": "switzerland",
    "tailândia": "thailand",
    "tais": "tajikistan",
    "tanzânia": "tanzania",
    "togo": "togo",
    "tonga": "tonga",
    "trinidad e tobago": "trinidad and tobago",
    "tunísia": "tunisia",
    "turquemenistão": "turkmenistan",
    "turquia": "turkey",
    "tuvalu": "tuvalu",
    "uganda": "uganda",
    "uruguai": "uruguay",
    "uzbequistão": "uzbekistan",
    "vanuatu": "vanuatu",
    "vaticano": "vatican city",
    "venezuela": "venezuela",
    "vietnam": "vietnam",
    "zâmbia": "zambia",
    "zimbábue": "zimbabwe"
}

# Função para buscar a bandeira do país usando a API Restcountries
def obter_bandeira(pais):
    # Converte o nome do país em português para o nome correto em inglês
    pais_ingles = mapa_paises.get(pais.lower())
    
    if not pais_ingles:
        return None

    url = f"https://restcountries.com/v3.1/name/{pais_ingles}?fullText=true"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Para garantir que a requisição foi bem-sucedida
        dados = resposta.json()
        bandeira_url = dados[0]['flags']['svg']  # URL da bandeira (formato SVG)
        return bandeira_url
    except Exception as e:
        return None

# Função do chatbot
def chatbot():
    st.write("Olá! Eu sou o Chatbot de Bandeiras. Me diga o nome de um país em português e eu mostro a bandeira dele.")
    
    st.write("Mateus Pereira Silva RA: 81788, Henrique Santos Rocha RA: 54370")

    pais = st.text_input("Qual país você quer ver a bandeira?")

    if pais:
        bandeira_url = obter_bandeira(pais)
        
        if bandeira_url:
            st.image(bandeira_url, caption=f"Aqui está a bandeira de {pais.capitalize()}", use_column_width=True)
        else:
            st.error("Desculpe, não consegui encontrar a bandeira desse país. Tente outro nome.")
    
# Inicia o chatbot
chatbot()