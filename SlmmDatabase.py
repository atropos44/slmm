from SlmmModItem import SlmmModItem

class SlmmDatabase(object):
    '''
    Main class for database access
    '''

    def __init__(self, db_file=None):
        self.db_file = db_file

    def getMods(self):
        return list()