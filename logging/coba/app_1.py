import logging
import auxiliary_module

# create logger with 'spam_application'
logger = logging.getLogger('app_1')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of aux.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of aux.Auxiliary')
logger.info('calling auxiliary_mod.do_something')
a.do_something()
logger.info('finished auxiliary_mod.do_something')
logger.info('calling a.some_function()')
auxiliary_module.some_function()
logger.info('done with auxle.some_function()')
