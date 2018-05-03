import unittest
from oars_gb_pkg.helpers.geo import dist_between_points#(p1, p2, earth_radius=6371e3)
import math
try:
    from geometry_msgs.msg import Pose2D
    from oars_gb.msg import WaypointList
except ImportError:
    from tests.mock_ros_msgs import Pose2D, WaypointList

class TestDistanceCalculator(unittest.TestCase):
    """
    Tests to see if Haversine distance formula is actually working
    """
    def set_up_test(self):
        self.pStart = (0,0)
        self.pEnd = (0,0)

    def test_two_points(self):
        self.pStart = (-71.271684, 42.298873)
        self.pEnd = (-71.281976, 42.300654)
        dist = dist_between_points(self.pStart, self.pEnd)
        print("THE DISTANCE IS", dist)
        self.assertEqual(dist, 0.8693*1000)


if __name__ == '__main__':
    # Run the tests
    unittest.main()