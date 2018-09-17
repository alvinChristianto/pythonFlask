import logging
import app_1
import app2


#create logger
logger = logging.getLogger('MAIN')
logger.setLevel(logging.DEBUG)

#create CONSOLE HANDLER and set level to warningI
log = logging.FileHandler('runlog.log')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

#create FORMATER
formatter = logging.Formatter('%(asctime)s -  %(name)s : %(levelname)s >> %(message)s')

#add formatter to CH
log.setFormatter(formatter)
ch.setFormatter(formatter)

#add ch to logger
logger.addHandler(log)
logger.addHandler(ch)

#app code
#setl = 1000
#batas = app_1.my_function()
#if setl < batas :
#    logger.info('logging ')
#elif setl > batas :
#    logger.info('value is %s' %batas)
#    logger.info('logging 2')
#else :
#    logger.info('no match!')
#eogger.error('logging on ERROR!')
#logger.critical('logging on CRITICAL!')

logger.info('app started!')
a = app_1.getTime()
app2.doingThing()
logger.info('create instance to app_1 getTime')
logger.info('calling app.gettimeThing')
a.getTimeThing()
app_1.some_function()
logger.info('finish app!')
