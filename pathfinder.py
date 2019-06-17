from PIL import image

class = ElevationMap:
    def __init__(self, elevations)
    self.elevations = elevations
    
def elevation_at_coordinate(self, x, y)
    return self.elevations[y][x]

def min elevation(self)
    return min([min(row) for row in self.elevations])

class = Path: