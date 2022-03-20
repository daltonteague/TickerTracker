import twitter
api = twitter.Api(consumer_key='5bQLhJ279zI53FYowT6GsA4ZV',
                  consumer_secret='SChDXOlyZHUNgfXCqxPmIoSE8bKu97LPss37N2NjJkFkaz841P',
                  access_token_key='1236393776987373569-oZreqgj9KPCItSeq8UaPeacP9TSnNT',
                  access_token_secret='GHV8BdUHN9smtxLQfQZ5iTAiL5oLsZiVkiGJaGjt4d9Kl')

results = api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2022-03-20&count=100")

print(results)