from dotenv import load_dotenv
import os
from typing import List,Dict, Optional
def load_env_varibles()->Optional[Dict[str,str]]:
    load_dotenv()
    api_key=os.getenv("API_KEY")
    print("Your API KEY IS:",api_key)

def main():
    env_vars=load_env_varibles()

if __name__ =="__main__":
    main()