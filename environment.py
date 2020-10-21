
ENV_URLS = {
    "dev": "https://api.spotify.com/"
}


def before_scenario(context, scenario):
    context.data = {}

    env = context.config.userdata.get('env')
    context.base_url = ENV_URLS[env]
    print(context.base_url)
