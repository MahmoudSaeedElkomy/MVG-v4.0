from mvg_production import MVGProduction, AIConfig, AIProvider
import json

def main():
    config = AIConfig(provider=AIProvider.MOCK)
    mvg = MVGProduction(config)
    query = "I tried this algorithm and got stuck on step 3, can you help?"
    res = mvg.process_request(query, user_id="test_user")
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
