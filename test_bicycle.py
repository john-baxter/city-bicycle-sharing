import unittest
import bicycle as bike

class TestBicycle(unittest.TestCase):
  def test_bicycle_is_instance_of_Bicycle(self):
    bicycle = bike.Bicycle()
    self.assertIsInstance(bicycle, bike.Bicycle)

  def test_a_bicycle_is_working(self):
    bicycle = bike.Bicycle()
    self.assertTrue(bicycle.is_working())




































































































if __name__ == "__main__":
    unittest.main(
      verbosity = 2,
    )