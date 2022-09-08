import random

def generate_coordinates():
    """Generate coordinates for the mediterrean sea."""
    coordinates = []

    latitude = "%.6f" % random.uniform(33, 38)
    longitude = "%.6f" % random.uniform(18, 25)

    coordinates.append((latitude, longitude))
    return coordinates