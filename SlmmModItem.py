class SlmmModItem(object):
    '''
    Models a Mod item
    '''

    def __init__(self, id=0, order=0, name='', status=''):
        self.id = id
        self.order = order
        self.name = name
        self.status = status

    def __str__(self):
        return 'Mod #{}: order={}, name={}, status={}'.format(self.id, self.order, self.name, self.status)