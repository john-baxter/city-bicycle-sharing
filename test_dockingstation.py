import unittest
import dockingstation as ds

class TestDockingStation(unittest.TestCase):
    def test_docking_station_is_instance_of_DockingStation(self):
        docking_station = ds.DockingStation()
        self.assertIsInstance(docking_station, ds.DockingStation)
    
    def test_docking_station_can_dock_bike(self):
        docking_station = ds.DockingStation()
        docking_station.dock("bike")
        self.assertEqual(docking_station.bikes[0], "bike")

    def test_docking_station_can_release_bike(self):
      docking_station = ds.DockingStation()
      docking_station.dock("bike")
      bike = docking_station.release()
      self.assertEqual(bike, "bike")

































































































if __name__ == "__main__":
    unittest.main(
      verbosity = 2,
    )
