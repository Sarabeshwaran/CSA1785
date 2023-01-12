

def play_alpha_beta(self):
     while True:
        self.draw_board()
        self.result = self.is_end()

        if self.result != None:
            if self.result == 'X':
                print('The winner is X!')
            elif self.result == 'O':
                print('The winner is O!')
            elif self.result == '.':
                print("It's a tie!")


            self.initialize_game()
            return

        if self.player_turn == 'X':

            while True:
                start = time.time()
                (m, qx, qy) = self.min_alpha_beta(-2, 2)
                end = time.time()
                print('Evaluation time: {}s'.format(round(end - start, 7)))
                print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                px = int(input('Insert the X coordinate: '))
                py = int(input('Insert the Y coordinate: '))

                qx = px
                qy = py

                if self.is_valid(px, py):
                    self.current_state[px][py] = 'X'
                    self.player_turn = 'O'
                    break
                else:
                    print('The move is not valid! Try again.')

        else:
            (m, px, py) = self.max_alpha_beta(-2, 2)
            self.current_state[px][py] = 'O'
            self.player_turn = 'X'
