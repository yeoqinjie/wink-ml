class WinkNetwork(object):
    def __init__(self):
        return


class Wink(object):
    def __init__(self, name, relation):
        self.name = name
        self.relation = relation
        self.score = 0

    def relate(self):
        self.score += 1

