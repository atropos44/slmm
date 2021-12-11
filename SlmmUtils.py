'''
File for SLMM utility functions
'''

import logging, logging.config, configparser

def getSlmmConfig():
    '''
    Reads SLMM config file
    '''

    config = configparser.ConfigParser()
    config.read('config.ini')

    logger = getSlmmLogger()
    logger.debug('Read config.ini file: {}'.format({section: dict(config[section]) for section in config.sections()}))

    return config

def getSlmmLogger():
    '''
    Returns SLMM logger
    '''
    
    logging.config.fileConfig('logger.ini')
    logger = logging.getLogger('SlmmLogger')
    return logger