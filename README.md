# twitter-text-mining

## Prerequisites

Make sure you have installed `pandas` and `matplotlib` package, using `pip`.

Also you need to have Twitter API credentials, such as:
* `ACCESS_TOKEN`
* `ACCESS_TOKEN_SECRET`
* `CONSUMER_KEY`
* `CONSUMER_SECRET`

Enter these credentials into `CREDENTIALS.json` in the format of

```
{
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET",
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_key": "YOUR_CONSUMER_SECRET"
}
```

## Build

Once the prerequisites are satisfied, listen to Twitter Streaming API and pipe the output.

```
python twitter_streaming.py > data/twitter_data.txt
```

Extract relevant links by executing the following:

```
python extract.py
```
