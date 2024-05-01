import unittest
import Poker

class TestPokerGame(unittest.TestCase):
    def test_HandRank(self):
        self.assertEqual(Poker.HandRank([1, 2, 3, 4, 13]), 6)  #Straight
        self.assertEqual(Poker.HandRank([0, 13, 26, 8, 1]), 7)  #3 of Kind
        self.assertEqual(Poker.HandRank([0, 2, 12, 39, 1]), 9)  #Pair
        self.assertEqual(Poker.HandRank([0, 1, 2, 3, 4]), 5) #Flush
        self.assertEqual(Poker.HandRank([0, 13, 26, 39, 14]), 3)  #4 of a Kind

    def test_DidPlayerWin(self):
        #the array on the left is player, the array on the right is dealer
        self.assertEqual(Poker.DidPlayerWinner([1,2,3,4,13],[5,6,7,8,9]),2)#Player win
        self.assertEqual(Poker.DidPlayerWinner([5,6,7,8,9],[1,2,3,4,13]),1)#Dealer Win
        self.assertEqual(Poker.DidPlayerWinner([5,6,7,8,9],[5,6,7,8,9]),3)#Tie
        
if __name__ == "__main__":
    unittest.main()

