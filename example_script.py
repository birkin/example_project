import logging, os, sys
import requests

## setup ------------------------------------
auth_key = os.environ['ES__AUTH_KEY']
print(f'in x() funtion; the auth-key is, ``{auth_key}``')

## create basicConfig logger with no file-writer
logging.basicConfig(
    level=logging.INFO,
    # format='%(asctime)s %(levelname)s %(message)s',
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
    handlers=[ logging.StreamHandler(sys.stdout) ]
)
log = logging.getLogger(__name__)
log.debug( 'test log entry' )


## ok real work ----------------------------

## make api-request
rsp = requests.get( 'https://api.weather.gov/gridpoints/OKX/33,34/forecast' )
json_data = rsp.json()

## parse out the fahrenheit temp
pass
f_temp = 32
pass

## convert to celsius
pass
c_temp = 0
pass
