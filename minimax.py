def minimax(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()

        best_score = float('-inf')
        for move in legal_moves:
            score = self.min_value(game.forecast_move(move), depth-1)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move if best_move else (-1,-1)

    def max_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return game.utility(self)

        if depth <= 0:
            return max([self.score(game.forecast_move(m), self) for m in legal_moves])

        best_score = float('-inf')
        for move in legal_moves:
            best_score = max([best_score, self.min_value(game.forecast_move(move), depth - 1)])

        return best_score

    def min_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return game.utility(self)

        if depth <= 0:
            return min([self.score(game.forecast_move(m), self) for m in legal_moves])

        best_score = float('inf')
        for move in legal_moves:
            best_score = min([best_score, self.max_value(game.forecast_move(move), depth - 1)])

        return best_score
