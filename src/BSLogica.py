from logic import *

class BSLogic:
    def __init__(self):
        # Definición de personajes como símbolos lógicos
        self.personajes = {
            "Moe": Symbol("Moe"),
            "Clancy": Symbol("Clancy"),
            "Chuck": Symbol("Chuck"),
            "Pearl": Symbol("Pearl"),
            "R_T": Symbol("R-T"),
            "Chester": Symbol("Chester"),
            "Eve": Symbol("Eve"),
            "Lola": Symbol("Lola"),
            "Colette": Symbol("Colette"),
            "Surge": Symbol("Surge"),
            "Bit_8": Symbol("8-Bit"),
            "Carl": Symbol("Carl"),
            "Tara": Symbol("Tara"),
            "Nita": Symbol("Nita"),
            "Spike": Symbol("Spike"),
            "Rico": Symbol("Rico"),
            "Cold": Symbol("Cold"),
            "Shelly": Symbol("Shelly"),
            "Draco": Symbol("Draco"),
            "Hank": Symbol("Hank"),
            "Buster": Symbol("Buster"),
            "Meg": Symbol("Meg"),
            "Ash": Symbol("Ash"),
            "Jacky": Symbol("Jacky"),
            "Bibi": Symbol("Bibi"),
            "Rosa": Symbol("Rosa"),
            "Frank": Symbol("Frank"),
            "Darryl": Symbol("Darryl"),
            "El_Primo": Symbol("El Primo"),
            "Bull": Symbol("Bull"),
            "Angelo": Symbol("Angelo"),
            "Maisie": Symbol("Maisie"),
            "Mandy": Symbol("Mandy"),
            "Bonnie": Symbol("Bonnie"),
            "Janet": Symbol("Janet"),
            "Belle": Symbol("Belle"),
            "Nani": Symbol("Nani"),
            "Bea": Symbol("Bea"),
            "Piper": Symbol("Piper"),
            "Brock": Symbol("Brock"),
            "Larry_Lawrie": Symbol("Larry & Lawrie"),
            "Grom": Symbol("Grom"),
            "Sprout": Symbol("Sprout"),
            "Tick": Symbol("Tick"),
            "Dynamike": Symbol("Dynamike"),
            "Barley": Symbol("Barley"),
            "Penny": Symbol("Penny"),
            "Charlie": Symbol("Charlie"),
            "Willow": Symbol("Willow"),
            "Otis": Symbol("Otis"),
            "Griff": Symbol("Griff"),
            "Squeak": Symbol("Squeak"),
            "Lou": Symbol("Lou"),
            "Amber": Symbol("Amber"),
            "Gale": Symbol("Gale"),
            "Mr_P": Symbol("Mr. P"),
            "Emz": Symbol("Emz"),
            "Sandy": Symbol("Sandy"),
            "Genio": Symbol("Genio"),
            "Bo": Symbol("Bo"),
            "Jessie": Symbol("Jessie"),
            "Kenji": Symbol("Kenji"),
            "Lily": Symbol("Lily"),
            "Melodie": Symbol("Melodie"),
            "Mico": Symbol("Mico"),
            "Cordelius": Symbol("Cordelius"),
            "Sam": Symbol("Sam"),
            "Fang": Symbol("Fang"),
            "Buzz": Symbol("Buzz"),
            "Stu": Symbol("Stu"),
            "Edgar": Symbol("Edgar"),
            "Leon": Symbol("Leon"),
            "Crow": Symbol("Crow"),
            "Mortis": Symbol("Mortis"),
            "Berry": Symbol("Berry"),
            "Kit": Symbol("Kit"),
            "Doug": Symbol("Doug"),
            "Gray": Symbol("Gray"),
            "Gus": Symbol("Gus"),
            "Ruffs": Symbol("Ruffs"),
            "Byron": Symbol("Byron"),
            "Max": Symbol("Max"),
            "Pam": Symbol("Pam"),
            "Poco": Symbol("Poco")
            
        }
        self.knowledge = []

    def agregar_sinergias(self, per_seleccionado):
        sinergias = {
            "Moe": ["Berry", "Doug", "Poco"],
            "Clancy": ["Shelly", "Bull", "El_Primo"],
            "Chuck": ["Mortis", "Crow", "Leon"],
            "Pearl": ["Rico", "Pam", "Piper"],
            "R_T": ["Clancy", "Shelly", "Carl"],
            "Chester": ["Edgar", "Mortis", "Buster"],
            "Eve": ["Janet", "Pam", "Gale"],
            "Lola": ["Piper", "Gray", "Nita"],
            "Colette": ["Mortis", "Edgar", "Leon"],
            "Surge": ["Angelo", "Max", "Meg"],
            "Bit_8": ["Penny", "Barley", "Tara"],
            "Carl": ["Rosa", "Jessie", "Bull"],
            "Tara": ["Sandy", "Poco", "Jessie"],
            "Nita": ["Tara", "Mortis", "Shelly"],
            "Spike": ["Crow", "Leon", "Rico"],
            "Rico": ["Pam", "Piper", "Carl"],
            "Cold": ["Shelly", "Rosa", "El_Primo"],
            "Shelly": ["Bull", "Carl", "Rosa"],
            "Draco": ["Rico", "Mortis", "Piper"],
            "Hank": ["Buster", "Rosa", "Bull"],
            "Buster": ["Frank", "Gale", "Hank"],
            "Meg": ["Surge", "Belle", "Janet"],
            "Ash": ["Bibi", "Jessie", "Shelly"],
            "Jacky": ["Rosa", "Bull", "El_Primo"],
            "Bibi": ["Jessie", "Shelly", "Rosa"],
            "Rosa": ["Jacky", "Carl", "Nita"],
            "Frank": ["Bull", "El_Primo", "Rosa"],
            "Darryl": ["Bull", "El_Primo", "Jessie"],
            "El_Primo": ["Bull", "Rosa", "Nita"],
            "Bull": ["Shelly", "El_Primo", "Rosa"],
            "Angelo": ["Surge", "Piper", "Max"],
            "Maisie": ["Buster", "Sprout", "Barley"],
            "Mandy": ["Mortis", "Edgar", "Leon"],
            "Bonnie": ["Shelly", "Bull", "El_Primo"],
            "Janet": ["Pam", "Meg", "Sandy"],
            "Belle": ["Gray", "Mortis", "Belle"],
            "Nani": ["Rico", "Shelly", "Jessie"],
            "Bea": ["Spike", "Leon", "Crow"],
            "Piper": ["Rico", "Nita", "Jessie"],
            "Brock": ["Poco", "Shelly", "Rico"],
            "Larry_Lawrie": ["Mortis", "Rico", "Spike"],
            "Grom": ["Shelly", "Jessie", "Piper"],
            "Sprout": ["Sprout", "Mr_P", "Lou"],
            "Tick": ["Mortis", "Crow", "Leon"],
            "Dynamike": ["Barley", "Rico", "Piper"],
            "Barley": ["Dynamike", "Mr_P", "Penny"],
            "Penny": ["Barley", "Mortis", "Rico"],
            "Charlie": ["Sprout", "Sandy", "Piper"],
            "Willow": ["Belle", "Janet", "Mortis"],
            "Otis": ["Buster", "Mortis", "Meg"],
            "Greliff": ["Penny", "Rico", "Sandy"],
            "Squeak": ["Penny", "Barley", "Dynamike"],
            "Lou": ["Mr_P", "Sandy", "Gale"],
            "Amber": ["Barley", "Mortis", "Jessie"],
            "Gale": ["Belle", "Gus", "Darryl"],
            "Mr_P": ["Lou", "Gus", "Sprout"],
            "Emz": ["Poco", "Mortis", "Edgar"],
            "Sandy": ["Tara", "Jessie", "Sprout"],
            "Genio": ["Piper", "Mortis", "Penny"],
            "Bo": ["Shelly", "Poco", "Nita"],
            "Jessie": ["Rico", "Tara", "Piper"],
            "Kenji": ["Pam", "Nita", "Piper"],
            "Lily": ["Jessie", "Tara", "Nita"],
            "Melodie": ["Barley", "Penny", "Mortis"],
            "Mico": ["Mortis", "Leon", "Crow"],
            "Cordelius": ["Surge", "Angelo", "Belle"],
            "Sam": ["Buster", "Penny", "Rico"],
            "Fang": ["Buzz", "Edgar", "Leon"],
            "Buzz": ["Fang", "Jessie", "Janet"],
            "Stu": ["Piper", "Rico", "Nita"],
            "Edgar": ["Mortis", "Meg", "Nita"],
            "Leon": ["Spike", "Mortis", "Crow"],
            "Crow": ["Spike", "Leon", "Mortis"],
            "Mortis": ["Edgar", "Mortis", "Leon"],
            "Berry": ["Buster", "Edgar", "Shelly"],
            "Kit": ["Tara", "Shelly", "Pam"],
            "Doug": ["Pam", "Nita", "Poco"],
            "Gray": ["Byron", "Belle", "Piper"],
            "Gus": ["Mr_P", "Gale", "Pam"],
            "Ruffs": ["Mortis", "Penny", "Janet"],
            "Byron": ["Poco", "Belle", "Gray"],
            "Max": ["Surge", "Meg", "Tara"],
            "Pam": ["Poco", "Piper", "Tara"],
            "Poco": ["Pam", "Piper", "Belle"]
            
        }

        if per_seleccionado in sinergias:
            for aliado in sinergias[per_seleccionado]:
                self.knowledge.append(self.personajes[aliado])

    def verificar_sinergias(self, equipo):
        sinergias_equipo = set()
        combined_knowledge = And(*self.knowledge)

        for personaje in equipo:
            if personaje in self.personajes:
                try:
                    if model_check(combined_knowledge, self.personajes[personaje]):
                        sinergias_equipo.add(personaje)
                except Exception as e:
                    print(f"Error verificando sinergias para {personaje}: {e}")

        return len(sinergias_equipo)

