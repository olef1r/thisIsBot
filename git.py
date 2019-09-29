import asyncio
import os

from octomachinery.github.api.tokens import GitHubOAuthToken
from octomachinery.github.api.raw_client import RawGitHubAPI


async def main():
    access_token = GitHubOAuthToken(os.environ["GITHUB_TOKEN"])
    gh = RawGitHubAPI(access_token, user_agent='webknjaz')
    res = await gh.post(
        '/repos/mariatta/strange-relationship/issues/207/reactions',
        preview_api_version='squirrel-girl',
        data={
            'content': 'heart'
        },
    )
    print(res)

asyncio.run(main())
