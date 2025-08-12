# 0. Create new enviornment done
# 1. find ip address done
# 2. find location_info done
# 3. api get airtraffic data done
# 4. send to sql done
# 5. present results with panda done
# 6. schedule using prefect
# 7. add to docker
# - move from config to .env

from flows.ingest_data import main

if __name__ == "__main__":
    main()