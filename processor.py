import sys, os, argparse
import logging

parser = argparse.ArgumentParser(description="load all args")
parser.add_argument('--parameter_file', help="Path to parameter file", required=True)
args = parser.parse_args()

## Logging Setups
logger = logging.getLogger("processor")
logger.setLevel(logging.INFO)
if not logger.handlers:
    # Stream Handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # File Handler
    file_handler = logging.FileHandler("processor.log", mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # Prevent propagation to root logger to avoid duplicate messages
    logger.propagate = False
logger.info("Logger is set")


logger.info(args)
logger.info(args.parameter_file)
logger.info(f"Arguments: {sys.argv}")
logger.info(f"temp: {os.environ.get('JAVA_HOME')}")
logger.info("Hello World")
 