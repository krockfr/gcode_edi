


class Voiture:


	def __init__(self, coul):
		self.couleur = coul
		self.marque = "renault"
		self.nb_porte = 5
		nom = "test"


	def changer_couleur(self, m_couleur):
		self.couleur = m_couleur




if __name__ == "__main__":
	
	mavoiture = Voiture("jaune")
	print mavoiture.couleur
	mavoiture.changer_couleur("rouge")
	print mavoiture.couleur
	
	mavoiture2 = Voiture("grise")
	print mavoiture2.couleur

