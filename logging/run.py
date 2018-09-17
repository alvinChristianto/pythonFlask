import logging
import app_1

#numeric_level = getattr(logging, loglevel.upper(), None)
#if not isinstance(numeric_level, int):
#    raise ValueError('Invalid log Level : %s' % loglevel)
FORMAT = "%(asctime)s : %(levelname)s >> %(message)s"
logging.basicConfig(
        filename='runlog.log',
        filemode ='w',
        format =FORMAT,
        level=logging.DEBUG)

def main():
    logging.basicConfig(
            filename='runlog.log',
            filemode ='w',
            format =FORMAT,
            level=logging.DEBUG)
    
    logging.info('logging on INFO!')
    logging.debug('logging on DEBUG!')
    logging.warning('logging on WARNING!')
    app_1.doingThing()
    logging.error('logging on error!')
    logging.critical('logging on critical!')

if __name__ == '__main__':
    main()


