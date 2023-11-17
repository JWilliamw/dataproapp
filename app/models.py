from app import db

class Collecte(db.Model):
    id_collecte = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(1000), nullable=True)
    prix = db.Column(db.Integer, nullable=True)

    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_enfants = db.Column(db.String(1000), index=True, unique=True)
    categorie_socioprofessionnelle = db.Column(db.String(1000), nullable=True)
    prix_panier = db.Column(db.Integer, nullable=True)
    id_collecte = db.Column(db.Integer, nullable=True)