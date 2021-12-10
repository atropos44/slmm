from SlmmModItem import SlmmModItem


class SlmmDatabase(object):
    '''
    Main class for database access
    '''

    def __init__(self, db_file=None):
        self.db_file = db_file

    def getMods(self):

        # begin test data
        test_mod = SlmmModItem(1, 'Test mod v1', 'Installed')
        return [test_mod]

        # end test data
        return list()