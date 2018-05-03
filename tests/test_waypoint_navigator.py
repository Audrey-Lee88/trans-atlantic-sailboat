import unittest
from oars_gb_pkg.nodes.thinking.waypoint_navigator import WaypointNavigator
try:
    from geometry_msgs.msg import Pose2D
    from oars_gb.msg import WaypointList
except ImportError:
    from tests.mock_ros_msgs import Pose2D, WaypointList


class TestWaypointGeneration(unittest.TestCase):
    """
    Tests the conversion of a list of GridMap
    cells to navigate into a list of GPS waypoints.
    """

    def setUp(self):
        self.test_position = Pose2D()

    def test_calculate_desired_heading(self):
        wn = WaypointNavigator(waypoint_radius=0.5, use_ros=False)
        self.test_position.x = 1
        self.test_position.y = 1
        test_waypoint_list = self.create_waypoint_list([(4, 4), (6, 6), (6, 8), (8, 8), (10, 8), (11, 11), (13, 13)])

        wn.update_location(self.test_position)
        print('HEY NOAH LOOK HERE', test_waypoint_list)
        wn.update_wp_list(test_waypoint_list)

        self.assertEqual(wn.calculate_desired_heading(), 45.0)

    def test_have_reached_wp_multiple(self):
        wn = WaypointNavigator(waypoint_radius=3, use_ros=False)
        test_waypoint_list = [(42.289917, -71.302917), (42.289925, -71.303192), (42.289811, -71.303239),
                              (42.289785, -71.303410), (42.289694, -71.303660), (42.289582, -71.303894)]
        wn.update_wp_list(self.create_waypoint_list(test_waypoint_list))

        # First test: Initialize at (0,0) just cause, then see if it recognizes the first waypoint
        self.test_position.x = 0
        self.test_position.y = 0
        wn.update_location(self.test_position)
        self.assertEqual(wn.next_wp, test_waypoint_list[0])

        # Second test: See if the waypoint updates once within waypoint radius
        self.test_position.x = 42.289916
        self.test_position.y = -71.302916
        wn.update_location(self.test_position)
        self.assertEqual(wn.next_wp, test_waypoint_list[1])

        # Third test: Same location, so next_wp ***should*** be the same in theory (but it don't be that way)
        wn.update_location(self.test_position)
        self.assertEqual(wn.next_wp, test_waypoint_list[1])

        # Fourth test
        self.test_position.x = 6
        self.test_position.y = 5
        wn.update_location(self.test_position)
        self.assertEqual(wn.next_wp, test_waypoint_list[2])

        # Fifth test
        self.test_position.x = 5
        self.test_position.y = 5
        wn.update_location(self.test_position)
        self.assertEqual(wn.next_wp, test_waypoint_list[2])

    @staticmethod
    def create_pose2d(x=0, y=0, theta=0):
        pos = Pose2D()
        pos.x = x
        pos.y = y
        pos.theta = theta
        return pos

    @staticmethod
    def create_waypoint_list(points):
        wl = WaypointList()
        for p in points:
            wl.longitudes.data.append(p[0])
            wl.latitudes.data.append(p[1])
        return wl


if __name__ == '__main__':
    # Run the tests
    unittest.main()
