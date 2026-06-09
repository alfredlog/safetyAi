# utils.py

def calculate_center(x1, y1, x2, y2):
    """
    Berechnet den Mittelpunkt einer Bounding Box.
    """

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    return center_x, center_y


def point_in_zone(
    x,
    y,
    zone_x1,
    zone_y1,
    zone_x2,
    zone_y2
):
    """
    Prüft, ob ein Punkt innerhalb
    einer Sicherheitszone liegt.
    """

    return (
        zone_x1 < x < zone_x2
        and
        zone_y1 < y < zone_y2
    )