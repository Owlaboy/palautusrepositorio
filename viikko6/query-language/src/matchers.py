class QueryBuilder:
    def __init__(self, query= None):
        self.queries = []

    def playsIn(self, team):
        self.queries.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self.queries.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self.queries.append(HasFewerThan(value, attr))
        return self

    def oneOf(self, *queries):
        self.queries.append(Or(*queries))
        return self

    def build(self):
        returnable = And(*self.queries)
        self.queries = []
        return returnable

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matcters = matchers

    def test(self, player):
        for matcher in self._matcters:
            if matcher.test(player):
                return True
        
        return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass
    
    def test(self, player):
        return True

class Not:
    def __init__(self, test:bool):
        self._test = test

    def test(self, player):
        return not self._test.test(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        return Not(HasAtLeast(self._value, self._attr)).test(player)
