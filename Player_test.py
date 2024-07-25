from Classes.Player import Player 
import unittest
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_data=('John', 'Doe', 32, 34, 'Forward', 'Association1')
        self.player=Player(*self.player_data)
    def test_player_Initialization(self):
        self.assertEqual(self.player.first_name,self.player_data[0])
        self.assertEqual(self.player.last_name,self.player_data[1])
        self.assertEqual(self.player.apt,self.player_data[2])
        self.assertEqual(self.player.set,self.player_data[3])
        self.assertEqual(self.player.position,self.player_data[4])
        self.assertEqual(self.player.national_association,self.player_data[5])
if __name__=="__main__":
    unittest.main()