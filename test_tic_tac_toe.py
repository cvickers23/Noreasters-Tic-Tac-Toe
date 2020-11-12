#import libraries
import main
import unittest

class Test_TestTicTacToe(unittest.TestCase):
    # @mock.patch('unittest.input', create=True)
    # def test_Symbol_Selection(self, mocked_input):
    #     mocked_input.side_effect = ["X","x","O","o"]
    #     main.first_turn_player_token = ""
    #     main.second_turn_player_token = ""
    #     self.assertEqual(main.choose_token(),main.first_turn_player_token)

    def test_random_players(self):
        total_player_1_first = 0
        total_player_2_first = 0
        #Run the choose_turn_order function 10000 times
        for _ in range(10000):
            #make the names of player 1 and player 2 p1 and p2 for testing
            order_list = main.choose_turn_order("p1", "p2")
            #if player 1 chosen to go first
            if order_list[0] == "p1":
                total_player_1_first += 1
            #if player 2 chosen to go first
            elif order_list[0] == "p2":
                total_player_2_first += 1

        #ensure that each player is chosen to go first approximately 50% of the time
        #there is a lot of leway in case the players are not chosen exactly 50% of the time due to the nature of random chance
        self.assertTrue(( 4000 <= total_player_1_first <= 6000) and (4000 <= total_player_2_first <= 6000))

if __name__ == "__main__":
    unittest.main()