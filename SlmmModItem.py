class SlmmModItem(object):
    '''
    Models a Mod item
    '''

    def __init__(self, order=0, name='', status=''):
        self.order = order
        self.name = name
        self.status = status

    def __str__(self):
        return '#{} {} [{}]'.format(self.order, self.name, self.status)