from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, session, send_from_directory
from functools import wraps
from app.models import Client, Collecte
import matplotlib.pyplot as plt
import psycopg2
import plotly.express as px
from decimal import Decimal
from app import db, app
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route("/display")
def display():
  """Affiche la page d'accueil."""
  connection = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="goldenline_db",
        user="postgres",
        password="FulaSpeechCorpora"
        )

  cursor = connection.cursor()

  # Dépenses total par catégorie
  cursor.execute("SELECT categorie, SUM(prix) AS total FROM collecte GROUP BY categorie;")
  donnees_categories = cursor.fetchall()

  # Dépense du panier moyen en fonction de la catégorie socioprofessionnelle
  cursor.execute("SELECT categorie_socioprofessionnelle, AVG(prix_panier) AS moyenne FROM client GROUP BY categorie_socioprofessionnelle;")
  donnees_moyennes = cursor.fetchall()

  print(f"Données moyennes {donnees_moyennes}")
  
  categories, means = zip(*donnees_moyennes)
  fig = px.bar(x=categories, y=means, labels={'y': 'Moyenne prix'}, title='Moyenne par catégorie socioprofessionelle')


    # Save the figure to a static image file
  if not os.path.exists("images"):
    os.mkdir("images")
  fig.write_image("images/dataviz.png", engine="kaleido")
  
  connection.close()
  # Retourne la page d'accueil
  return render_template("display.html")


@app.route("/export")
def export():
  """Affiche la page d'export."""

  # Récupère les données de la base de données
  connection = psycopg2.connect("host=localhost dbname=goldenline_db user=postgres password=postgres")
  cursor = connection.cursor()

  # Récupère les données de la table collecte
  cursor.execute("SELECT * FROM collecte;")
  donnees = cursor.fetchall()

  # Ferme la connexion à la base de données
  connection.close()

  # Crée un tableau Pandas
  df = pd.DataFrame(donnees, columns=["id", "id_collecte", "categorie", "prix"])

  # Enregistre le tableau Pandas en tant que fichier CSV
  df.to_csv("collecte.csv")

  # Retourne la page d'export
  return render_template("export.html", donnees=donnees)

if __name__ == "__main__":
  app.run(debug=True)