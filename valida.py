from dotenv import load_dotenv
load_dotenv()

import os
print(repr(os.getenv("MLFLOW_TRACKING_URI")))