import subprocess
from aws_lambda_powertools import Logger

logger = Logger()

def handler(event, context): 
  try: 
    command = '/opt/awscli/aws sts get-caller-identity'
    resp = subprocess.run(command, shell=True,check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    logger.info(resp.stdout)
  except subprocess.CalledProcessError as e:
    logger.error(e.stderr)
    raise e
  