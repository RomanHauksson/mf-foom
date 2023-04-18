# MF FOOM

I fine-tuned GPT-3 on the lyrics of 96 MF DOOM songs to write rap lyrics in his style. The results aren't great but may improve if I retried using a bigger model.

## Example

Input prompt:

> A song titled "Metal Mask" about the story of how MF DOOM obtained his iconic metal mask and the power it gives him in the rap game.


Output:

```
Metal Mask Lyrics[Intro]
DOOM!
(What? You wanna give me some shit?)
Yeah, I got a thing for you (what?)
[Verse 1: MF DOOM]

I'm the master of this mask, and I use it to hide my face
The metal mask keeps me on the edge of sanity
That's when I'm at home with my girl, or in a club with my man
I might as well be playing Secret Agent Man (Secret Agent...man!)
At the same time, I can do anything that a normal person could do
For instance, if somebody was coming after me with a gun (Gun!) then you know what I'd do? (I'd blast 'em! Gun!) You already know what I'd do? Well for real though...it gives me powers in this rap game!

[Hook: MF DOOM + (Produced by MF DOOM)]
The metal mask keeps me on the edge of sanity
I might as well be playing Secret Agent Man (Secret Agent...man!)
At the same time, I can do anything that a normal person could do
For instance, if somebody was coming after me with a gun (Gun!) then you know what I'd do? (I'd blast 'em! Gun) You already know what I'd do? Well for real though...it gives me powers in this rap game!
The metal mask keeps me on the edge of sanityYou might also likeEmbedShare1Embed1 233Embed0You might also like29Embed2 1.8KFollowers›Mike Tyson is back to square one›Mike Tyson says he wants his first child to be named "Tyson"6 EmbedsBrandy Deol's brother arrested for DUI in NY7Embeds23Embeds11Embedly34Shared1This video has been shared(Produced by MF DOOM)15Sub hate rhymes3:2443 EmbarsMF DOOM grew up listening to stories about how he obtained his iconic metal mask and how it gave him all kinds of
```

## Workflow

1. `lyrics.py` downloads the lyrics of every MF DOOM song from Genius.com and saves them to lyrics.json.
2. `prompts.py` generates a one-sentence summary of each song and uses each summary–lyrics pair to generate fine-tuning prompts, which it saves in `prompts.jsonl`.
3. I ran `openai api fine_tunes.create -t prompts.jsonl -m babbage` in the terminal to fine-tune a GPT-3 Babbage model on the prompts and then generated an example in the OpenAI API Playground.