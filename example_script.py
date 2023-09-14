import logging, os, sys
import requests

print( 'starting' )
## setup ------------------------------------
auth_key = os.environ['ES__AUTH_KEY']
# print(f'in x() funtion; the auth-key is, ``{auth_key}``')

## create basicConfig logger with no file-writer
logging.basicConfig(
    level=logging.DEBUG,
    # format='%(asctime)s %(levelname)s %(message)s',
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
    handlers=[ logging.StreamHandler(sys.stdout) ]
)
log = logging.getLogger(__name__)
log.debug( 'test log entry' )


## ok real work ----------------------------\

def manage_work():

    ## make api-request
    data = make_api_request()

    ## parse out the fahrenheit temp
    f_temp = parse_out_fahrenheit_temp( data )

    ## convert to celsius
    c_temp = convert_to_celsius(f_temp)
    
    log.debug( f'c_temp, ``{c_temp}``' )
    return c_temp


def make_api_request():
    return 'foo'


def parse_out_fahrenheit_temp( the_data ):
    x = the_data[0]
    return 32

def convert_to_celsius( f_temp ):
    """ 
    Returns celsius temp as int 

    Usage:
    >>> convert_to_celsius( 32 )
    0
    """
    return 0


if __name__ == '__main__':
    manage_work()
