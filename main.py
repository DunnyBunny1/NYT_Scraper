from config.config import Config

def main(): 
    conf : Config = Config()
    print(f'Key:{conf.nyt_api_key}')
    print(f'URL:{conf.top_stories_base_url}')


if __name__ == '__main__':
    main()