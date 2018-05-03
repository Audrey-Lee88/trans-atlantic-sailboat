class Pose2D:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0


class Float32:

    def __init__(self):
        self.data = float(0)


class WaypointList:

    def __init__(self):
        self.latitudes = Float32MultiArray()
        self.longitudes = Float32MultiArray()


class Float32MultiArray:

    def __init__(self):
        self.data = []
