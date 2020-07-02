import unittest
import dockingstation as ds
# from dockingstation import DockingStation as ds

class TestDockingStation(unittest.TestCase):
    def test_docking_station_is_instance_of_DockingStation(self):
        docking_station = ds.DockingStation()
        self.assertIsInstance(docking_station, ds.DockingStation)
    
    # def test_docking_station_can_release_bike(self):
    #   docking_station = ds.DockingStation()
      































































































if __name__ == "__main__":
    unittest.main(
      verbosity = 2,
    )
