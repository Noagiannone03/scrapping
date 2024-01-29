import urllib.request
import re
import ssl

url = "https://xyz.wookafr.org/streaming/thriller/fast-and-furious/"

try:
    # Désactiver la vérification du certificat SSL
    ssl_context = ssl._create_unverified_context()

    # Envoyer une requête GET pour récupérer le contenu de la page
    with urllib.request.urlopen(url, context=ssl_context) as response:
        # Vérifier si la requête a réussi (code de statut 200)
        if response.getcode() == 200:
            # Lire le contenu de la réponse
            html_content = response.read().decode('utf-8')

            # Utiliser une expression régulière pour extraire l'élément iframe
            iframe_match = re.search(r'<iframe[^>]*>.*?</iframe>', html_content, re.DOTALL)

            if iframe_match:
                # Afficher l'élément iframe
                print(iframe_match.group(0))
            else:
                print("Aucun élément iframe trouvé sur la page.")
        else:
            print("La requête a échoué avec le code de statut : {response.getcode()}")
except Exception as e:
    print("Une erreur s'est produite : {e}")
