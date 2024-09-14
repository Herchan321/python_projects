def nombre_bits_necessaires(besoins):
    resultats = []
    for besoin in besoins:
        if besoin >= 2 and besoin <= 4:
            resultats.append(2)
        elif besoin > 4 and besoin <= 8:
            resultats.append(3)
        elif besoin > 8 and besoin <= 16:
            resultats.append(4)
        elif besoin > 16 and besoin <= 32:
            resultats.append(5)
        elif besoin > 32 and besoin <= 64:
            resultats.append(6)
        elif besoin > 64 and besoin <= 128:
            resultats.append(7)
        else:
            resultats.append(8)

    return resultats

def masque_vers_bits(masque):
  """Convertit un masque de sous-réseau en nombre de bits disponibles."""
  octets_masque = masque.split('.')
  bits_disponibles = 0
  for octet in octets_masque:
    bits_disponibles += int(octet)
  return bits_disponibles

def adresse_reseau(adresse, masque):
  """Calcule l'adresse réseau d'un sous-réseau."""
  octets_adresse = adresse.split('.')
  octets_masque = masque.split('.')
  reseau_octets = []
  for i in range(len(octets_adresse)):
    reseau_octets.append(str(int(octets_adresse[i]) & int(octets_masque[i])))
  return '.'.join(reseau_octets)

def adresse_broadcast(adresse_reseau, masque):
  """Calcule l'adresse broadcast d'un sous-réseau."""
  octets_reseau = adresse_reseau.split('.')
  octets_masque = masque.split('.')
  broadcast_octets = []
  for i in range(len(octets_reseau)):
    broadcast_octets.append(str(int(octets_reseau[i]) | int(octets_masque[i])))
  return '.'.join(broadcast_octets)

def nombre_hotis_disponibles(masque):
  """Calcule le nombre d'hôtes disponibles sur un sous-réseau."""
  bits_disponibles = masque_vers_bits(masque)
  return 2 ** bits_disponibles - 1



def nombre_bits_necessaires(besoins):
    resultats = []
    for besoin in besoins:
        if besoin >= 2 and besoin <= 4:
            resultats.append(2)
        elif besoin > 4 and besoin <= 8:
            resultats.append(3)
        elif besoin > 8 and besoin <= 16:
            resultats.append(4)
        elif besoin > 16 and besoin <= 32:
            resultats.append(5)
        elif besoin > 32 and besoin <= 64:
            resultats.append(6)
        elif besoin > 64 and besoin <= 128:
            resultats.append(7)
        else:
            resultats.append(8)

    return resultats

def masque_vers_bits(masque):
  """Convertit un masque de sous-réseau en nombre de bits disponibles."""
  octets_masque = masque.split('.')
  bits_disponibles = 0
  for octet in octets_masque:
    bits_disponibles += int(octet)
  return bits_disponibles

def adresse_reseau(adresse, masque):
  """Calcule l'adresse réseau d'un sous-réseau."""
  octets_adresse = adresse.split('.')
  octets_masque = masque.split('.')
  reseau_octets = []
  for i in range(len(octets_adresse)):
    reseau_octets.append(str(int(octets_adresse[i]) & int(octets_masque[i])))
  return '.'.join(reseau_octets)

def adresse_broadcast(adresse_reseau, masque):
  """Calcule l'adresse broadcast d'un sous-réseau."""
  octets_reseau = adresse_reseau.split('.')
  octets_masque = masque.split('.')
  broadcast_octets = []
  for i in range(len(octets_reseau)):
    broadcast_octets.append(str(int(octets_reseau[i]) | int(octets_masque[i])))
  return '.'.join(broadcast_octets)

def nombre_hotis_disponibles(masque):
  """Calcule le nombre d'hôtes disponibles sur un sous-réseau."""
  bits_disponibles = masque_vers_bits(masque)
  return 2 ** bits_disponibles - 1

def generer_sous_reseaux(adresse, masque, besoins):
    """Génère des sous-réseaux en respectant la limite de 255 par octet et les besoins spécifiques."""
    sous_reseaux = []
    adresses_hotes = []
    adresse_reseau = adresse_reseau(adresse, masque)
    masque_vers_bits = masque_vers_bits(masque)
    bits_par_sous_reseau = masque_vers_bits

    for besoin in besoins:
        # Calculer le nombre de bits nécessaires pour ce besoin
        bits_necessaires = nombre_bits_necessaires(besoin)

        # Si le nombre de bits nécessaires est supérieur au masque actuel, ajuster le masque
        while bits_necessaires > bits_par_sous_reseau:
            bits_par_sous_reseau += 1

        # Calculer le masque de sous-réseau du sous-réseau actuel
        masque_sous_reseau_bin = "1" * bits_par_sous_reseau + "0" * (32 - bits_par_sous_reseau)
        masque_sous_reseau = ".".join([str(int(masque_sous_reseau_bin[i:i+8], 2)) for i in range(0, 32, 8)])

        # Calculer l'adresse broadcast du sous-réseau actuel
        adresse_broadcast_sous_reseau = adresse_broadcast(adresse_reseau, masque_sous_reseau)

        # Ajouter le sous-réseau à la liste des sous-réseaux
        sous_reseaux.append((adresse_reseau, adresse_broadcast_sous_reseau))

        # Générer les adresses IP de tous les hôtes dans ce sous-réseau
        adresses_hote_sous_reseau = []
        for j in range(1, besoin + 1):
            adresse_hote = '.'.join(adresse_reseau.split('.')[:-1]) + '.' + str(j)
            adresses_hote_sous_reseau.append(adresse_hote)
        adresses_hotes.append(adresses_hote_sous_reseau)

        # Mettre à jour l'adresse réseau pour le prochain sous-réseau
        adresse_reseau = str(int(adresse_broadcast_sous_reseau.split('.')[0]) + 1) + ".0.0.0"

    return sous_reseaux, adresses_hotes


# Adresse IP de départ et masque de sous-réseau
adresse_ip_de_depart = '192.168.0.0'
masque_sous_reseau = '255.255.255.0'

# Besoins en nombre d'hôtes pour chaque sous-réseau
besoins_hotes = [50, 25, 25, 100, 10]

# Génération des sous-réseaux
sous_reseaux, adresses_hotes = generer_sous_reseaux(adresse_ip_de_depart, masque_sous_reseau, besoins_hotes)

# Affichage des sous-réseaux générés et des adresses des hôtes
for i, (sous_reseau, adresses) in enumerate(zip(sous_reseaux, adresses_hotes)):
    print(f"Sous-réseau {i+1}:")
    print(f"Adresse réseau: {sous_reseau[0]}")
    print(f"Adresse broadcast: {sous_reseau[1]}")
    print(f"Adresses des hôtes:")
    for adresse in adresses:
        print(adresse)
    print()














