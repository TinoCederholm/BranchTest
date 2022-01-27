# X-funktio tarkistaa onko kulma suora

def suorakulma(sivuA, sivuB, lavistaja):
    """"Tarkistaa suorakulmaisuuden käyttäen pythagoran lausetta

    Args:
        Args sivuA (float): Ensimmäisen pituus
        Args sivuB (float): Toisen pituus
        lavistaja (float): Lävistäjän mitta

    Returns:
        boolean : TRUE-> suorakulma
    """
    A_nelio = sivuA * sivuA
    B_nelio = sivuB * sivuB
    l_nelio = lavistaja * lavistaja

    if A_nelio + B_nelio == l_nelio:
        suora = True
    else:
        suora = False
    return suora

    # Testataan, että toimii
vastaus = suorakulma(3, 4, 5)
print (vastaus)


