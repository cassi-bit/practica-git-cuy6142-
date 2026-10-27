import requests

# Se solicita el nombre al usuario en lugar de dejarlo estático
nombre = input("Ingresa el nombre del Pokémon que deseas buscar: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"[cite: 1]

respuesta = requests.get(url, timeout=10)[cite: 1]
print(f"Código HTTP: {respuesta.status_code}")[cite: 1]
respuesta.raise_for_status()[cite: 1]
datos = respuesta.json()[cite: 1]

print(f"Nombre: {datos['name'].title()}")[cite: 1]
print(f"Peso: {datos['weight']} hectogramos")[cite: 1]
print("Habilidades:")[cite: 1]
for habilidad in datos["abilities"]:[cite: 1]
    print(f" - {habilidad['ability']['name']}")[cite: 1]
