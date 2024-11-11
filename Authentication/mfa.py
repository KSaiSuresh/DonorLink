import pyotp
import logging
import base64
from log_config import setup_logger

logger = setup_logger()
#logging.basicConfig(level=logging.DEBUG)

key = base64.b64decode('S2FtYWtzaGlwZWV0YW1kb25hdGlvbmFwcG1mYQ==').decode('ascii')
#logger.info(f'key value - {key}')

totp_auth = pyotp.totp.TOTP( 
  key).provisioning_uri( 
  name='Sai Suresh Karra', 
  issuer_name='Donation Admin')

def generate_otp(key):
    totp=pyotp.TOTP(key)
    return totp.now()

def verify_otp(otp, key=key):
    try:
      totp=pyotp.TOTP(key)
      logger.info(f'verify_otp response: {totp.verify(otp)}')
      return ({"mfa":str(totp.verify(otp))})
    except Exception:
       logger.exception(f'excepption occured while verfing otp')
       return ({"mfa":"False"})