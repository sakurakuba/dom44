class BaseDatabase:
    history_list = []

    @classmethod
    def list(cls):
        return cls.history_list

    @classmethod
    def add(cls, entity):
        #cls.history_list.sort()
        id = len(cls.history_list) + 1
        d = {id: entity}
        cls.history_list.append(d)
