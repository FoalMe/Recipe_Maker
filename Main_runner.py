from Flask import Flask , render_template , request
import requests

APP = Recipe_Maker

# Fuction to fetch results from the API
# Add API key with the website

def get_recipe(ingredients):
   API_key = " API_ key "
   Endpoint = "example.com"
   params =
   {
   "ingredients" : ingredients
   "API_key" : API_key
   }

response = response.get(endpoint, params = params)

if response.status_code == 200:
    return response.json()
else:
     return None

# Route to the home page
# Attach the html template

def search():
    ingredients = request.form['ingredients']
    recipes = get_recipes(ingredients)
    if recipes:
              return render_template( index.html , recipes = recipes)
    else:
         return 'Error fetching recipes'

def run():
    if __name__ = '__main__':
      app.run(debug = True)
     else: 
          return None
    
    
